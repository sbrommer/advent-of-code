map_ = [*open(0)]

w = len(map_)

plots = {complex(r, c): char
         for r, row in enumerate(map_)
         for c, char in enumerate(row)
         if char in '.S'}


def solve(goal):
    positions = {p for p, c in plots.items() if c == 'S'}
    ns = []
    offset = goal % w

    for i in range(goal):
        if i % w == offset:
            ns.append(len(positions))

        if len(ns) >= 4:
            d, c, b, a = ns[-4:]
            if not a - 3 * b + 3 * c - d:
                i = (goal - i) // w
                return a + i * (a - b) + (i * (i+1) // 2 * (a - 2 * b + c))

        positions = {p + d for p in positions
                     for d in {-1, 1, -1j, 1j}
                     if complex((p+d).real % w, (p+d).imag % w) in plots}

    return len(positions)


if w == 11:
    print(solve(6))
    print(solve(5000))

if w == 131:
    print(solve(64))
    print(solve(26501365))
