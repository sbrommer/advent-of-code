from heapq import heappop as pop, heappush as push

# Parse
grid = {x+y*1j: c
        for y, l in enumerate(open(0))
        for x, c in enumerate(l.strip())}

E, = [p for p, c in grid.items() if c == 'E']
S, = [p for p, c in grid.items() if c == 'S']
G  = {p for p, c in grid.items() if c != '#'}

# Solve
seen, q = set(), [(0, i:=0, [S], 1)]
best, tiles = 1e9, set()

while q:
    c, _, path, d = pop(q)
    p = path[-1]

    if c > best:
        break

    if p == E:
        if c < best:
            best, tiles = c, set()
        tiles |= {*path}

    for dc, r in [(1, 1), (1001, 1j), (1001, -1j)]:
        d_new = d*r
        p_new = p+d_new
        if p_new in G and (p_new, d_new) not in seen:
            push(q, (c+dc, i:=i+1, path+[p_new], d_new))

    seen |= {(p, d)}

print(best, len(tiles))
