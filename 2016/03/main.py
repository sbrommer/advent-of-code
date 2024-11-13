from more_itertools import chunked
from itertools import chain


def valid(sides):
    sides = sorted(sides)
    return sides[0] + sides[1] > sides[2]


def solve(triangles):
    return sum(map(valid, triangles))


def transform(triangles):
    return chain(*[chunked(col, 3) for col in zip(*triangles)])


triangles = [[*map(int, line.split())] for line in open(0)]

print(solve(triangles), solve(transform(triangles)))
