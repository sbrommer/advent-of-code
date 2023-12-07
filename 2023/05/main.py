from re import findall
from functools import reduce


def parse():
    seeds, *maps = open(0).read().split('\n\n')
    return parse_seeds(seeds), [parse_map(m) for m in maps]


def parse_seeds(seeds):
    return [int(seed) for seed in findall(r'\d+', seeds)]


def parse_map(m):
    m = [[int(d) for d in ds] for ds in findall(r'(\d+) (\d+) (\d+)', m)]
    return [[ds[0] - ds[1], ds[1], ds[1] + ds[2]] for ds in m]


def apply_map(seeds, m):
    mapped = []

    for diff, src_start, src_end in m:
        unmapped = []

        while seeds:
            seed_start, seed_end = seeds.pop()

            # left
            if seed_start < src_start:
                unmapped += [[seed_start, min(seed_end, src_start)]]

            # right
            if src_end < seed_end:
                unmapped += [[max(seed_start, src_end), seed_end]]

            # mid
            if seed_start < src_end and src_start < seed_end:
                mapped += [[diff + max(seed_start, src_start),
                            diff + min(seed_end, src_end)]]

        seeds = unmapped

    return mapped + seeds


def solve(seeds, maps):
    locations = sum([reduce(apply_map, maps, [seed]) for seed in seeds], [])
    return min(locations)[0]


seeds, maps = parse()

seeds1 = [(s, s + 1) for s in seeds]
seeds2 = [(s, s + l) for s, l in zip(seeds[::2], seeds[1::2])]

print(solve(seeds1, maps), solve(seeds2, maps))
