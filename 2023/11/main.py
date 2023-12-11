from itertools import combinations
from operator import sub


def empties(universe):
    return [r for r, row in enumerate(universe)
            if not row.count('#')]


def expand(galaxies, m):
    def expand_line(es, l):
        n = sum(e < l for e in es)
        return l + n * (m - 1)

    rs = empties(universe)
    cs = empties(zip(*universe))

    return [(expand_line(rs, r),
             expand_line(cs, c)) for r, c in galaxies]


def shortest_path(pair):
    return sum(map(abs, map(sub, *pair)))


def solve(galaxies, m):
    galaxies = expand(galaxies, m)
    pairs = combinations(galaxies, 2)
    return sum(map(shortest_path, pairs))


universe = [*open(0)]

galaxies = [(r, c)
            for r, row in enumerate(universe)
            for c, space in enumerate(row)
            if space == '#']

print(solve(galaxies, 2), solve(galaxies, 1000000))
