from functools import cache
from itertools import starmap


def parse_line(line):
    row, groups = line.split()
    groups = tuple(map(int, groups.split(',')))
    return row + '.', groups


def unfold(row, groups):
    return (row[:-1] + '?') * 4 + row, groups * 5


@cache
def solve(r, gs):
    if not gs:
        return '#' not in r

    if not r:
        return 0

    g = gs[0]
    return (r[0] != '#') * solve(r[1:], gs) + \
           ('.' not in r[:g] and r[g] in '?.') * solve(r[g+1:], gs[1:])


def solve_all(records):
    return sum(starmap(solve, records))


records = [*map(parse_line, open(0))]

print(solve_all(records), solve_all(starmap(unfold, records)))
