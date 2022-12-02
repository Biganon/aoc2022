with open("input", "r") as f:
    lines = f.read().splitlines()

# A : rock
# B : paper
# C : scissors

# X : I need to lose
# Y : draw
# Z : I need to win

outcomes = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1,
}

total = 0

for line in lines:
    outcome = outcomes[line]
    total += outcome

print(total)
