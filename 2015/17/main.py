import re
from itertools import combinations

# Parse
cs = list(map(int, re.compile(r'-?\d+').findall(open(0).read())))
l = len(cs)


# Helper function
def count(i):
    return sum(sum(c) == 150 for c in combinations(cs, i))


def counts():
    return map(count, range(l))


# Part 1
print(sum(counts()))

# Part 2
print(next(filter(lambda c: c, counts()), None))
