from operator import ne


def diff(line1, line2):
    return sum(map(ne, line1, line2))


def find_reflection(pattern, d):
    for i in range(1, len(pattern)):
        left = pattern[i-1::-1]
        right = pattern[i:]
        if sum(map(diff, left, right)) == d:
            return i
    return 0


def summarize(pattern, d):
    return find_reflection(pattern, d) * 100 + \
           find_reflection([*zip(*pattern)], d)


def solve(patterns, d=0):
    return sum(summarize(pattern, d) for pattern in patterns)


patterns = [pattern.split() for pattern in open(0).read().split('\n\n')]

print(solve(patterns), solve(patterns, 1))
