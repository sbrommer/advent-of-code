from collections import defaultdict
from itertools import pairwise

starts = [*map(int, open(0))]


def next(n):
    n ^= n <<  6 & 0xFFFFFF
    n ^= n >>  5 & 0xFFFFFF
    n ^= n << 11 & 0xFFFFFF
    return n


secret_sum, D = 0, defaultdict(int)

for n in starts:
    ns = [n] + [n := next(n) for _ in range(2000)]
    prices = [n%10 for n in ns]
    changes = [b-a for a, b in pairwise(prices)]
    patterns = [tuple(changes[i:i+4]) for i in range(len(prices)-4)]

    secret_sum += ns[-1]

    seen = set()
    for pattern, price in zip(patterns, prices[4:]):
        if pattern not in seen:
            D[pattern] += price
            seen |= {pattern}

print(secret_sum, max(D.values()))
