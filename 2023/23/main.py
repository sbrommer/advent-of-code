from collections import defaultdict

G = {complex(r, c): char
     for r, row in enumerate(open(0))
     for c, char in enumerate(row.strip())
     if char != '#'}

start = [*G][0]
end = [*G][-1]

dirs = {'^': {-1}, 'v': {1}, '<': {-1j}, '>': {1j}, '.': {-1, 1, -1j, 1j}}


def neighbours(v):
    return {v + d for d in {-1, 1, -1j, 1j}} & G.keys()


V = {start, end} | {v for v in G if len(neighbours(v)) >= 3}

E_ = {v: {v + d for d in dirs[G[v]]
          if v + d in G and d in dirs[G[v + d]]}
      for v in G}

E = defaultdict(set)
weights = {}

for u in V - {end}:
    for v in E_[u]:
        path = [u, v]
        while v not in V:
            v = list(E_[v] - set(path))[0]
            path += [v]
        weights[(u, v)] = len(path) - 1
        E[u] |= {v}


def DFS(u, d=0, visited=set()):
    if u == end:
        return d
    if u in visited:
        return 0

    return max(DFS(v, d + weights[(u, v)], visited | {u}) for v in E[u])


print(DFS(start))

items = list(E.items())
for u, vs in items:
    for v in vs:
        E[v] |= {u}

weights = weights | {(v, u): w for (u, v), w in weights.items()}

print(DFS(start))
