from itertools import accumulate

dirs = {'U': -1, 'D': 1, 'R': 1j, 'L': -1j,
        '3': -1, '1': 1, '0': 1j, '2': -1j}


def shoelace(x, y):
    return int(x.real * y.imag - x.imag * y.real)


def parse_line(line):
    d, m, c = line.split()
    dig1 = dirs[d] * int(m)
    dig2 = dirs[c[7]] * int(c[2:7], 16)
    return dig1, dig2


def dig(dig_plan):
    steps = int(sum(map(abs, dig_plan)))
    path = [*accumulate(dig_plan)]
    area = sum(map(shoelace, path, path[1:]))

    return abs(area // 2) + 1 + steps // 2


dig_plans = zip(*map(parse_line, open(0)))
print(*map(dig, dig_plans))
