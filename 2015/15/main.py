from re import findall
import numpy as np

results = [[*map(int, findall(r'-?\d+', line))] for line in open(0)]

ingrs = np.matrix([r[:-1] for r in results])
cals = np.array([r[-1] for r in results])


def score(ams):
    return np.product(np.maximum(ams * ingrs, 0))


def amounts():
    ams = []
    for i in range(101):
        for j in range(100-i):
            for k in range(100-i-j):
                ams.append(np.array([i, j, k, 100-i-j-k]))
    return ams


print(max(map(score, amounts())),
      max(score(ams) for ams in amounts() if ams @ cals == 500))
