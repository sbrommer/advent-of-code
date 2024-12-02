from itertools import combinations


def parse(text=open(0)):
    return [[*map(int, line.split())] for line in text]


def ssa(r): # strictly slowly ascending
    return all(1 <= x - y <= 3 for x, y in zip(r, r[1:]))


def is_safe(r, dampened=False):
    rs = [r]
    if dampened:
        rs += [*combinations(r, len(r)-1)]
    return any(ssa(r) or ssa(r[::-1]) for r in rs)


data = parse()

print(sum(map(is_safe, data)),
      sum([is_safe(report, True) for report in data]))
