with open("input", "r") as f:
    grid = f.read().splitlines()

visible = 0

for y, row in enumerate(grid):
    for x, tree in enumerate(row):
        current = grid[y][x]
        north = [grid[my][x] for my in range(0, y)]
        south = [grid[my][x] for my in range(y + 1, len(grid))]
        west = [grid[y][mx] for mx in range(0, x)]
        east = [grid[y][mx] for mx in range(x + 1, len(row))]
        if (
            (not any(x for x in north if x >= current))
            or (not any(x for x in south if x >= current))
            or (not any(x for x in west if x >= current))
            or (not any(x for x in east if x >= current))
        ):
            visible += 1

print(visible)
