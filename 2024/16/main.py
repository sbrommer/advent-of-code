from heapq import heappop as pop, heappush as push

# Parse
grid = {x+y*1j: c
        for y, l in enumerate(open(0))
        for x, c in enumerate(l.strip())}

E, = [p for p, c in grid.items() if c == 'E']
S, = [p for p, c in grid.items() if c == 'S']
G  = [p for p, c in grid.items() if c != '#']

# Solve
seen, q = set(), [(0, i := 0, S, 1, {S})]
best, tiles = 1e9, set()

while q:
    c, _, p, d, path = pop(q)

    if c > best:
        break

    if p == E:
        if c < best:
            best, tiles = c, set()
        tiles |= path

    for dc, r in [(1, 1), (1001, 1j), (1001, -1j), (2001, -1)]:
        d_new = d*r
        p_new = p+d_new
        if p_new in G and (p_new, d_new) not in seen:
            push(q, (c+dc, i:=i+1, p_new, d_new, path | {p_new}))

    seen |= {(p, d)}

print(best, len(tiles))
