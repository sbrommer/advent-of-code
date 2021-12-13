from statistics import mode
from collections import Counter

# Parse
input = list(map(list, open(0).read().split('\n')))[:-1]


# Helper functions
def least_common(xs):
    return Counter(xs).most_common()[-1][0]


# Transpose input
input = [i for i in zip(*input)]

# Part 1
print(''.join(map(mode, input)))

# Part 2
print(''.join(map(least_common, input)))
