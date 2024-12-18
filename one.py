#!env python3

left = []
right = []

with open('one.txt', mode = 'r', encoding='utf-8') as f:
    for line in f:
        for l,r in line.split():
            left.append(l)
            right.append(r)

total = 0
for l , r in left,right:
    total += abs(l - r)

print(total)

