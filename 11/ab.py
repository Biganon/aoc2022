from math import lcm

with open("input", "r") as f:
    lines = f.read().splitlines()

class Monkey:
    def __init__(self, items):
        self.items = items
        self.inspections = 0
    def __repr__(self):
        return f"Monkey ({self.items})"

monkeys = []

for line in lines:
    if "Starting items" not in line:
        continue
    items = list(map(int, line.split(":")[1].split(",")))
    monkeys.append(Monkey(items=items))

idx = 0
for line in lines:
    if "Operation" not in line:
        continue
    operation = line.split("=")[1].strip()
    monkeys[idx].operation = operation
    idx += 1

idx = 0
for line in lines:
    if "Test" not in line:
        continue
    divisor = int(line.split("by")[1])
    monkeys[idx].divisor = divisor
    idx += 1

idx = 0
for line in lines:
    if "If true" not in line:
        continue
    if_true = int(line.split("monkey")[1])
    monkeys[idx].if_true = if_true
    idx += 1

idx = 0
for line in lines:
    if "If false" not in line:
        continue
    if_false = int(line.split("monkey")[1])
    monkeys[idx].if_false = if_false
    idx += 1

rounds = 10000
xanax = 1
divisor_lcm = lcm(*(m.divisor for m in monkeys))

for idx_round in range(rounds):
    for monkey in monkeys:
        while monkey.items:
            wl = monkey.items.pop(0)
            wl %= divisor_lcm
            monkey.inspections += 1
            result = eval(monkey.operation.replace("old", str(wl)))
            result //= xanax
            if result % monkey.divisor == 0:
                monkeys[monkey.if_true].items.append(result)
            else:
                monkeys[monkey.if_false].items.append(result)

sorted_monkeys = sorted(monkeys, key=lambda m:m.inspections, reverse=True)
monkey_business = sorted_monkeys[0].inspections * sorted_monkeys[1].inspections
print(monkey_business)