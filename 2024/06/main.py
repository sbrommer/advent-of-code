def parse(text=open(0)):
    G = {x+y*1j: c
         for y, line in enumerate(text)
         for x, c    in enumerate(line.strip())}

    ps = {*G.keys()}
    os = {p for p, c in G.items() if c == '#'}
    g, = [p for p, c in G.items() if c == '^']

    return ps, os, g


def patrol(ps, os, p):
    d = -1j
    visits, seen = set(), set()

    while p in ps and (p, d) not in seen:
        visits |= {p}
        seen   |= {(p, d)}

        if p+d in os:
            d *= 1j
        else:
            p += d

    return visits, (p, d) in seen


ps, os, g = parse()
visits = patrol(ps, os, g)[0]
loops = sum(patrol(ps, os | {o}, g)[1] for o in visits - {g})

print(len(visits), loops)
