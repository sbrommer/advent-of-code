from itertools import combinations

# Parse
containers = [*map(int, open(0))]


# Helper function
def count(i):
    return sum(sum(c) == 150 for c in combinations(containers, i))


def counts():
    return map(count, range(len(containers)))


print(*counts())

# Part 1
print(sum(counts()))

# Part 2
print(min(filter(lambda c: c, counts())))
