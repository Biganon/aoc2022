import re

with open("input", "r") as f:
    lines = f.read().splitlines()

stacks = lines[:8]
stacks = list(zip(*stacks[::-1]))
stacks = [[c for c in s if c != " "] for i, s in enumerate(stacks) if (i - 1) % 4 == 0]

moves = lines[10:]

for move in moves:
    r = re.search(r"move (\d+) from (\d+) to (\d+)", move)
    a = int(r.group(1))
    f = int(r.group(2))
    t = int(r.group(3))

    for i in range(a):
        c = stacks[f - 1].pop()
        stacks[t - 1].append(c)

print("".join([stack[-1] for stack in stacks]))
