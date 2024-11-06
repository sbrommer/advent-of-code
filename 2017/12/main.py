inp = [line.strip().split(' <-> ') for line in open(0).readlines()]

G = {int(p): [int(c) for c in cs.split(', ')] for p, cs in inp}


def DFS(u=0):
    visited = set()
    q = [u]

    while q:
        v = q.pop()
        visited |= {v}
        q += [w for w in G[v] if w not in visited]

    return visited


vs = set(G)
n = 0
while vs:
    vs -= DFS(vs.pop())
    n += 1

print(len(DFS()), n)
