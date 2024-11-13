from more_itertools import chunked
from operator import eq


def cover_up(state, l):
    while len(state) < l:
        state = step(state)

    return checksum(state[:l])


def step(a):
    b = [1 - i for i in a[::-1]]
    return a + [0] + b


def checksum(s):
    while not len(s) % 2:
        s = [eq(*chunk) for chunk in chunked(s, 2)]

    return ''.join(map(lambda b: str(int(b)), s))


state = [int(i) for i in input()]

print(cover_up(state, 272), cover_up(state, 35651584))
