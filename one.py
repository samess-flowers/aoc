#!env python3

left = []
right = []

with open("one.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        bort = line.split()
        left.append(int(bort[0]))
        right.append(int(bort[1]))

left.sort()
right.sort()

total = 0
for i, _ in enumerate(left):
    total += abs(left[i] - right[i])

print(total)
