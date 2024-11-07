start_A = int(input().split()[-1])
start_B = int(input().split()[-1])


def generator_(value, factor, d=1):
    def next_value(): return (value * factor) % 2147483647

    while True:
        value = next_value()
        while value % d:
            value = next_value()
        yield bin(value)[-16:]


def generator(G, picky=False):
    if G == 'A':
        return generator_(start_A, 16807, 4 if picky else 1)

    return generator_(start_B, 48271, 8 if picky else 1)


def judge(G1, G2, n):
    return sum(next(G1) == next(G2) for _ in range(n))


print(judge(generator('A'), generator('B'), 40_000_000),
      judge(generator('A', True), generator('B', True), 5_000_000))
