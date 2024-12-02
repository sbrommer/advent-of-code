import re
from collections import defaultdict


def parse(text=open(0)):
    claims = defaultdict(set)

    for line in text:
        i, X, Y, W, H = parse_ints(line)
        for x in range(W):
            for y in range(H):
                claims[(X+x, Y+y)] |= {i}

    return claims


def parse_ints(line):
    return map(int, re.findall(r'\d+', line))


def overlapping(claims):
    return [c for c in claims.values() if len(c) >= 2]


def not_overlapping(claims):
    return set.union(*claims.values()) - set.union(*overlapping(claims))


claims = parse()

print(len(overlapping(claims)),
      [*not_overlapping(claims)][0])
