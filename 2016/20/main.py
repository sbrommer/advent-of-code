def solve(ranges, part1=True):
    m = 0
    t = 0

    for l, h in ranges:
        if m < l:
            if part1:
                return m

            t += l - m

        m = max(m, h + 1)

    return 4294967296 + t - m


ranges = [tuple(map(int, line.split('-'))) for line in open(0)]
ranges.sort()

print(solve(ranges), solve(ranges, False))
