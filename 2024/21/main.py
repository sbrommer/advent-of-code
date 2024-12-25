from itertools import pairwise, product, accumulate
from functools import cache

cat = ''.join


def make_pad(list):
    return {c: x+y*1j
            for y, r in enumerate(list)
            for x, c in enumerate(r)
            if c != '.'}


def shortest_paths(f, t, pad):
    f, t = pad[f], pad[t]

    def valid(path):
        ps = [*accumulate([f]+path)]
        return ps[-1] == t and not {*ps} - {*pad.values()}

    l = int(abs((t-f).real) + abs((t-f).imag))

    paths = map(list, product([-1, 1, -1j, 1j], repeat=l))

    return [tuple(path+['A']) for path in paths if valid(path)]


def paths(list):
    pad = make_pad(list)
    return {(f, t): shortest_paths(f, t, pad) for f in pad for t in pad}


codes = [line.strip() for line in open(0)]

numpaths = paths(['789', '456', '123', '.0A'])
dirpaths = paths([['.', -1j, 'A'], [-1, 1j, 1]])


@cache
def length(path, d, num=False):
    paths = numpaths if num else dirpaths

    if d == 0:
        return len(path)

    return sum(min(length(p, d-1)
                   for p in paths[f, t])
               for f, t in pairwise(['A']+[*path]))


def complexities(code, d):
    return length(tuple(code), d+1, True) * int(code[:-1])


print(*[sum(complexities(code, d) for code in codes) for d in [2, 25]])
