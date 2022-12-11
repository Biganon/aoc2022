with open("input", "r") as f:
    lines = f.read().splitlines()

durations = {"addx":2, "noop":1}
checkpoints = (20, 60, 100, 140, 180, 220)

x = 1
cycle = 0
sum_ = 0

for line in lines:
    parts = line.split(" ")
    operation = parts[0]
    for _ in range(durations[operation]):
        cycle += 1
        if cycle in checkpoints:
            sum_ += cycle*x
    if operation == "addx":
        value = int(parts[1])
        x += value

print(sum_)