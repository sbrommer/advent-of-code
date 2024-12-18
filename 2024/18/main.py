def parse_line(line):
    return complex(*eval(line))


bits = [*map(parse_line, open(0))]
memory = {x+y*1j for x in range(71) for y in range(71)}


def path(t):
    unseen = memory - {*bits[:t]}

    q = [(0, 0)]
    for l, p in q:
        if p in unseen:
            if p == 70+70j:
                return l

            q += [(l+1, p+d) for d in [-1, 1, -1j, 1j]]
            unseen -= {p}

    return 0


def time(a=0, b=len(bits)-1):
    if a+1 == b:
        return bits[a]

    m = a + ((b-a) // 2)

    return time(a, m) if not path(m) else time(m, b)


print(path(1024), time())
