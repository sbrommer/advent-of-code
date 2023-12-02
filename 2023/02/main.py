from re import findall
from math import prod
from collections import defaultdict


def f(game):
    nr = int(findall(r'\d+', game)[0])
    m = min_cubes(game)

    part1 = nr if valid(m) else 0
    part2 = prod(m.values())

    return part1, part2


def min_cubes(sets):
    m = defaultdict(int)
    for n, colour in findall(r'(\d+) (\w+)', sets):
        m[colour] = max(m[colour], int(n))
    return m


def valid(m):
    return m['red'] <= 12 and m['green'] <= 13 and m['blue'] <= 14


print(*map(sum, zip(*map(f, open(0).readlines()))))
