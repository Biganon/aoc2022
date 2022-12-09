with open("input", "r") as f:
    grid = f.read().splitlines()

ss = []

for y, row in enumerate(grid):
    for x, tree in enumerate(row):
        current = grid[y][x]
        north = [grid[my][x] for my in range(0, y)][::-1]
        south = [grid[my][x] for my in range(y + 1, len(grid))]
        west = [grid[y][mx] for mx in range(0, x)][::-1]
        east = [grid[y][mx] for mx in range(x + 1, len(row))]
        vn = 0
        vs = 0
        vw = 0
        ve = 0
        for t in north:
            vn += 1
            if t >= current:
                break
        for t in south:
            vs += 1
            if t >= current:
                break
        for t in west:
            vw += 1
            if t >= current:
                break
        for t in east:
            ve += 1
            if t >= current:
                break
        ss.append(vn * vs * vw * ve)

print(max(ss))
