with open("input", "r") as f:
    grid = f.read().splitlines()

sy = grid.index([r for r in grid if "S" in r][0])
sx = grid[sy].index("S")

visited = set()

visited.add((sx, sy))

class Node:
    def __init__(self, x, y, cost, heur):
        self.x = x
        self.y = y
        self.cost = cost
        self.heur = heur

start = Node(x=sx, y=sy, cost=0, heur=0)

