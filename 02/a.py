with open("input", "r") as f:
    lines = f.read().splitlines()

# A / X : rock
# B / Y : paper
# C / Z : scissors

outcomes = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3,
}

total = 0

for line in lines:
    outcome = outcomes[line]
    total += outcome

print(total)
