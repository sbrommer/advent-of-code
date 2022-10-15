from parse import search


def part1(n, ranges):
    m = 0
    for l, h in ranges:
        if m < l:
            return m
            break
        else:
            m = max(m, h + 1)


def part2(n, ranges):
    m = 0
    t = 0
    for l, h in ranges:
        if m < l:
            t += l - m
        m = max(m, h + 1)

    return t + n + 1 - m


n = 4294967295

ranges = [tuple(search('{:d}-{:d}', line)) for line in open(0).readlines()]
ranges.sort()

print(part1(n, ranges))
print(part2(n, ranges))
