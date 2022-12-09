from math import sqrt, floor

with open("input", "r") as f:
    lines = f.read().splitlines()

length = 2

parts = [[0, 0] for _ in range(length)]
visited_by_tail = set()

deltas = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}

for line in lines:
    direction = line[0]
    steps = int(line[2:])
    for step in range(steps):
        delta = deltas[direction]
        parts[0][0] += delta[0]
        parts[0][1] += delta[1]

        for part_idx in range(1, len(parts)):
            distance = floor(
                sqrt(
                    (parts[part_idx - 1][0] - parts[part_idx][0]) ** 2
                    + (parts[part_idx - 1][1] - parts[part_idx][1]) ** 2
                )
            )
            if distance <= 1:
                pass
            else:
                if parts[part_idx - 1][0] > parts[part_idx][0]:
                    parts[part_idx][0] += 1
                if parts[part_idx - 1][0] < parts[part_idx][0]:
                    parts[part_idx][0] -= 1
                if parts[part_idx - 1][1] > parts[part_idx][1]:
                    parts[part_idx][1] += 1
                if parts[part_idx - 1][1] < parts[part_idx][1]:
                    parts[part_idx][1] -= 1

        visited_by_tail.add(tuple(parts[-1]))

print(len(visited_by_tail))
