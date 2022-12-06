with open("input", "r") as f:
    chars = f.read()

length = 14

for i in range(len(chars) - length):
    subset = chars[i : i + length]
    if len(set(subset)) == length:
        print(i + length)
        break
