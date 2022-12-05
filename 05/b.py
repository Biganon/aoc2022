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

    s = stacks[f - 1][-a:]
    stacks[f - 1] = stacks[f - 1][:-a]
    stacks[t - 1] = stacks[t - 1] + s

print("".join([stack[-1] for stack in stacks]))
