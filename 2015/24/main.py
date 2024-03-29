from itertools import combinations
from math import prod

ws = [*map(int, open(0))]

for n in [3, 4]:
    for r in range(len(ws)):
        groups = [g for g in combinations(ws, r) if sum(g) == sum(ws) // n]
        if groups:
            break

    print(min(map(prod, groups)))
