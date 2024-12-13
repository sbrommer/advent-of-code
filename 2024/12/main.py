def parse(text=open(0)):
    return {x+y*1j: c
            for y, l in enumerate(text)
            for x, c in enumerate(l.strip())}


def get_region(G, p):
    r, q = set(), {p}

    while q:
        p = q.pop()
        r |= {p}
        q |= {p+d for d in [-1, 1, -1j, 1j]
              if G.get(p+d) == G[p]} - r

    return r


def get_regions(G):
    ps, rs = set(G), []

    while ps:
        r = get_region(G, ps.pop())
        ps -= r
        rs += [r]

    return rs


def perimiter(r, p, d):
    return p in r and p+d not in r


def side(r, p, d):
    return perimiter(r, p, d) and not perimiter(r, p+d*1j, d)


def count(rs, P):
    return sum(len(r)
               for r in rs
               for p in r
               for d in [-1, 1, -1j, 1j]
               if P(r, p, d))


G = parse()
regions = get_regions(G)

print(count(regions, perimiter), count(regions, side))
