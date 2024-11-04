from math import sqrt
from collections import defaultdict


def manhattan(n):
    cycle = int(sqrt(n - 1) + 1) // 2
    first = (2 * cycle - 1) ** 2 + 1
    offset = n - first
    mid = cycle + first - 1 + offset // (2 * cycle) * (2 * cycle)
    return cycle + abs(n - mid)


def neighbours_sum(spiral, c):
    neighbours = [
        c + complex(i, j)
        for i in [-1, 0, 1]
        for j in [-1, 0, 1]
        if (i, j) != (0, 0)
    ]

    return sum(spiral[n] for n in neighbours)


def cycle_coords(cycle):
    return [complex(c, cycle)  for c in range( cycle-1, -cycle-1, -1)] + \
           [complex(-cycle, c) for c in range( cycle-1, -cycle-1, -1)] + \
           [complex(c, -cycle) for c in range(-cycle+1,  cycle+1)] + \
           [complex(cycle, c)  for c in range(-cycle+1,  cycle+1)]


def first_sum(n):
    spiral = defaultdict(int)
    spiral[0+0j] = 1
    cycle = 0

    while True:
        for c in cycle_coords(cycle):
            s = neighbours_sum(spiral, c)
            if s > n:
                return s
            spiral[c] = s
        cycle += 1


n = int(input())

print(manhattan(n), first_sum(n))
