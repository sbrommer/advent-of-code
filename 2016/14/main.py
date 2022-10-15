from hashlib import md5
from functools import cache
from re import search


@cache
def hash(i, n):
    h = f'ihaygndm{i}'
    for _ in range(n + 1):
        h = md5(h.encode()).hexdigest()
    return h


def three(h):
    return search(r'(.)\1\1', h)


def five(h, t):
    return 5 * t in h


def find(n=0):
    k = 1
    i = 0

    while k <= 64:
        if not (t := three(hash(i, n))) is None:
            for j in range(i+1, i+1001):
                if five(hash(j, n), t[0][0]):
                    if k == 64:
                        return i
                    k += 1
                    break
        i += 1


print(find())
print(find(2016))
