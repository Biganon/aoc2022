with open("input", "r") as f:
    lines = f.read().splitlines()

sums = []
top = 1

current = 0
for line in lines:
    if line:
        current += int(line)
    else:
        sums.append(current)
        current = 0

print(sum(sorted(sums)[-top:]))
