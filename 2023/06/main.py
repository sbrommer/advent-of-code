from re import findall
from math import prod, sqrt, ceil, floor


def parse_ints(line):
    return map(int, findall(r'\d+', line))


def parse(inp):
    return map(parse_ints, inp)


def n_ways(t, d):
    x1, x2 = [2 * d / (t + s * sqrt(t ** 2 - 4 * d)) for s in [1, -1]]
    return ceil(x2) - floor(x1) - 1


def solve(races):
    return prod(map(n_ways, *races))


paper = list(open(0).readlines())
unkerned = [i.replace(' ', '') for i in paper]

print(*[solve(parse(i)) for i in [paper, unkerned]])
