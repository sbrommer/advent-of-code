from collections import Counter
from itertools import starmap, permutations

cat = ''.join


def parse(text=open(0)):
    return [line.strip() for line in text]


def checksum(ids):
    counters = [Counter(i) for i in ids]
    twos   = len([c for c in counters if 2 in c.values()])
    threes = len([c for c in counters if 3 in c.values()])
    return twos * threes


def similar(i1, i2):
    return cat(c1 for c1, c2 in zip(i1, i2) if c1 == c2)


def common_letters(ids):
    similars = starmap(similar, permutations(ids, 2))
    return max(similars, key=len)


ids = parse()

print(checksum(ids), common_letters(ids))
