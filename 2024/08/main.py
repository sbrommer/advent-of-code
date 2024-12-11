from itertools import permutations
from collections import defaultdict


def parse(text=open(0)):
    freqs = defaultdict(set)

    for y, line in enumerate(text):
        for x, c in enumerate(line.strip()):
            freqs[c] |= {x+y*1j}

    ps = set.union(*freqs.values())
    freqs = [f for c, f in freqs.items() if c != '.']

    return ps, freqs


ps, freqs = parse()

def antinodes(part1=True, ps=ps, freqs=freqs):
    r = [1] if part1 else range(int(len(ps)**0.5))

    return len(ps & {
        a+i*(a-b)
        for antennas in freqs
        for a, b     in permutations(antennas, 2)
        for i        in r
    })

print(antinodes(), antinodes(False))
