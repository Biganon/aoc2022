with open("input", "r") as f:
    lines = f.read().splitlines()

durations = {"addx":2, "noop":1}

sx = 1
px = 0
py = 0
lit = set()

for line in lines:
    parts = line.split(" ")
    operation = parts[0]
    for _ in range(durations[operation]):
        if px in range(sx-1, sx+2):
            lit.add((px, py))
        px += 1
        if px > 39:
            px = 0
            py += 1

    if operation == "addx":
        value = int(parts[1])
        sx += value

for y in range(6):
    for x in range(40):
        if (x, y) in lit:
            print("#", end="")
        else:
            print(" ", end="")
    print()