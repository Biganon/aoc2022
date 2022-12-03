from string import ascii_lowercase, ascii_uppercase

priorities = ascii_lowercase + ascii_uppercase

with open("input", "r") as f:
    lines = f.read().splitlines()

total = 0

nb_groups = int(len(lines) / 3)

for idx in range(nb_groups):
    a, b, c = map(set, lines[idx * 3 : idx * 3 + 3])
    same = list(a.intersection(b).intersection(c))[0]
    total += priorities.index(same) + 1

print(total)
