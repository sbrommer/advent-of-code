from re import finditer
from math import prod

schematic = open(0).readlines()

symbols = {(r, c): set()
           for r in range(len(schematic))
           for c in range(len(schematic[0]))
           if schematic[r][c] not in '0123456789.\n'}


def adjacent_symbols(r, s):
    return {(y, x)
            for y in [r-1, r, r+1]
            for x in range(s[0]-1, s[1]+1)
            if (y, x) in symbols.keys()}


for r, line in enumerate(schematic):
    for match in finditer(r'\d+', line):
        for gear in adjacent_symbols(r, match.span()):
            symbols[gear].add(int(match[0]))

print(sum(sum(ns) for ns in symbols.values()),
      sum(prod(ns) for ns in symbols.values() if len(ns) == 2))
