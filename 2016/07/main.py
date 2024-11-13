# Imports
import re
from more_itertools import distribute, windowed


def parse(line):
    parts = re.split(r'[\[\]]', line.strip())
    ips, hns = distribute(2, parts)
    return list(ips), list(hns)


def ps(xs, n):
    return [''.join(w[:2])
            for x in xs for w in windowed(x, n)
            if w == w[::-1] and w[0] != w[1]]


def has_abba(xs): return bool(ps(xs, 4))
def get_abas(xs): return set(ps(xs, 3))
def get_babs(xs): return set([aba[::-1] for aba in ps(xs, 3)])


inp = [parse(line) for line in open(0)]

tls = sum(has_abba(ips) and not has_abba(hns) for ips, hns in inp)
ssl = sum(bool(get_abas(ips) & get_babs(hns)) for ips, hns in inp)

print(tls, ssl)
