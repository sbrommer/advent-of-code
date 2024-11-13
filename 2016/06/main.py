from statistics import mode
from collections import Counter

signal = [*zip(*open(0))][:-1]


def least_common(xs):
    return Counter(xs).most_common()[-1][0]


def message(f):
    return ''.join(map(f, signal))


print(*map(message, [mode, least_common]))
