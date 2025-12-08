from math import dist, prod
from itertools import combinations


boxes = [tuple(map(int, l.split(','))) for l in open(0)]

parent = {b: b for b in boxes}
size = {b: 1 for b in boxes}


def find(b):
    if parent[b] == b:
        return b

    return find(parent[b])


def union(b1, b2):
    b1, b2 = find(b1), find(b2)

    if b1 != b2:
        parent[b1] = b2
        size[b2] += size[b1]
        size[b1] = 0


pairs = sorted(combinations(boxes, 2), key=lambda b: dist(*b))

for i, (b1, b2) in enumerate(pairs, 1):
    union(b1, b2)

    # Part 1
    if i == 1000: # Use 10 for test input.
        print(prod(sorted(size.values())[-3:]))

    # Part 2
    if len(size) in size.values():
        print(b1[0] * b2[0])
        break
