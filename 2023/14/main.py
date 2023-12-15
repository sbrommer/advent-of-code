def transpose(platform):
    return map(''.join, [*zip(*platform)])


def tilt(platform, rev=True):
    return ['#'.join(''.join(sorted(rock, reverse=rev))
            for rock in row.split('#')) for row in platform]


def load(platform):
    return sum((len(row) - i) * (rock == 'O')
               for row in platform for i, rock in enumerate(row))


def cycle(platform):
    for r in [1, 1, 0, 0]:
        platform = tilt(transpose(platform), r)
    return platform


platform = [line.strip() for line in open(0)]

# Part 1
print(load(tilt(transpose(platform))))


# Part 2
def solve(platform):
    n = 1_000_000_000
    cache = []

    while platform not in cache:
        cache.append(platform)
        platform = cycle(platform)

    i = cache.index(platform)
    return cache[i + (n - i) % (len(cache) - i)]


print(load(transpose(solve(platform))))
