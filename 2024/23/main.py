from collections import defaultdict
from itertools import permutations

G = defaultdict(set)
for line in open(0):
    f, t = line.strip().split('-')
    G[f] |= {t}
    G[t] |= {f}

cliques3 = {tuple(sorted([u, v, w]))
            for u in G
            if u[0] == 't'
            for v, w in permutations(G[u], 2)
            if w in G[v]}


def BronKerbosch(R, P, X):
    if not P and not X:
        return {tuple(R)}

    cliques = set()

    for v in [*P]:
        cliques |= BronKerbosch(R | {v}, P & G[v], X & G[v])
        P -= {v}
        X |= {v}

    return cliques


cliques = BronKerbosch(set(), {*G.keys()}, set())
party, = [c for c in cliques if len(c) == max(map(len, cliques))]
password = ','.join(sorted(party))

print(len(cliques3), password)
