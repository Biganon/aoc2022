from string import ascii_lowercase, ascii_uppercase

priorities = ascii_lowercase + ascii_uppercase

with open("input", "r") as f:
    lines = f.read().splitlines()

total = 0

for line in lines:
    half = int(len(line) / 2)
    first = set(line[:half])
    second = set(line[half:])
    both = list(first.intersection(second))[0]
    total += priorities.index(both) + 1

print(total)
