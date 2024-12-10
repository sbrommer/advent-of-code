tmap = {x+y*1j: int(n)
        for y, l in enumerate(open(0))
        for x, n in enumerate(l.strip())}

trails = set()
q = {(p,) for p, n in tmap.items() if n == 0}

while q:
    trail, *q = q
    v = trail[-1]

    if tmap[v] == 9:
        trails |= {trail}

    else:
        q += {tuple([*trail] + [v+dv])
              for dv in {-1, 1, -1j, 1j} if
              tmap.get(v+dv) == tmap[v] + 1}

print(len({(t[0], t[-1]) for t in trails}), len(trails))
