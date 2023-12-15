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


def key(platform):
    return ''.join(platform)


platform = [line.strip() for line in open(0)]

# Part 1
print(load(tilt(transpose(platform))))

# Part 2
n = 1_000_000_000
cache = {key(platform): 0}

for i in range(n):
    platform = cycle(platform)
    k = key(platform)
    if k not in cache:
        cache[k] = i
    else:
        for _ in range((n - i) % (i - cache[k]) - 1):
            platform = cycle(platform)
        break

print(load(transpose(platform)))
