with open("input", "r") as f:
    lines = f.read().splitlines()

rock = set()
sand = set()

# Build the map :

for line in lines:
    parts = [list(map(int, p.split(","))) for i, p in enumerate(line.split(" ")) if i%2 == 0]
    for idx in range(len(parts)-1):
        f = parts[idx]
        t = parts[idx+1]
        dx = t[0] - f[0]
        dx = dx//abs(dx) if dx != 0 else 0
        dy = t[1] - f[1]
        dy = dy//abs(dy) if dy != 0 else 0
        while f != t:
            rock.add(tuple(f))
            f[0] += dx
            f[1] += dy
        rock.add(tuple(f))

# Drop the sand :

bottom = max(rock, key=lambda x:x[1])[1] + 2
bottom_is_solid = False
genesis = (500,0)
unit = genesis
while True:
    # Part 1 test :
    if unit[1] > bottom:
            print(len(sand))
            bottom_is_solid = True
            unit = genesis
            continue
    # Part 2 test :
    if genesis in sand:
        print(len(sand))
        break
    # Movement :
    goals = ((unit[0], unit[1]+1), (unit[0]-1, unit[1]+1), (unit[0]+1, unit[1]+1))
    could_move = False
    for goal in goals:
        if (goal not in rock) and (goal not in sand) and (goal[1] != bottom or not bottom_is_solid):
            unit = goal
            could_move = True
            break
    if not could_move:
        sand.add(unit)
        unit = genesis