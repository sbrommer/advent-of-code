from functools import cmp_to_key


def parse(text = open(0).read()):
    por, updates = [part.split() for part in text.split('\n\n')]
    updates = [u.split(',') for u in updates]
    return por, updates


def mid(xs):
    return int(xs[len(xs) // 2])


por, updates = parse()
key = cmp_to_key(lambda x, y: -1 if f'{x}|{y}' in por else 1)

part1, part2 = 0, 0
for u in updates:
    s = sorted(u, key=key)
    part1 += (u == s) * mid(s)
    part2 += (u != s) * mid(s)

print(part1, part2)
