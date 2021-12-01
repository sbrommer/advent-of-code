import re
import numpy as np

# Parse input
rgx = re.compile(r'-?\d+')
results = [list(map(int, rgx.findall(line))) for line in open(0)]

ingrs = np.matrix([r[:-1] for r in results])
cals = np.array([r[-1] for r in results])

# Functions
def score(ams):
    return np.product(np.maximum(ams * ingrs, 0))


def amounts():
    ams = []
    for i in range(101):
        for j in range(100-i):
            for k in range(100-i-j):
                ams.append(np.array([i, j, k, 100-i-j-k]))
    return ams


# Part 1
print(max(map(score, amounts())))

# Part 2
print(max([score(ams) for ams in amounts() if ams @ cals == 500]))
