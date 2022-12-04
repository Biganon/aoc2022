with open("input", "r") as f:
    lines = f.read().splitlines()

number = 0
for line in lines:
    ra, rb = line.split(",")
    fa, ta = map(int, ra.split("-"))
    fb, tb = map(int, rb.split("-"))
    ra = set(range(fa, ta + 1))
    rb = set(range(fb, tb + 1))
    ri = ra.intersection(rb)
    if ri:
        number += 1

print(number)
