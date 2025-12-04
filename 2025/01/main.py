cat = ''.join


def parse_line(l):
    d, *n = l
    return [-1, 1][d == 'R'], int(''.join(n))


rotations = map(parse_line, open(0).readlines())

ans1, ans2 = 0, 0
p = 50

for d, r in rotations:
    for _ in range(r):
        p += d
        ans2 += not p % 100
    ans1 += not p % 100

print(ans1, ans2)
