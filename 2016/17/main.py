from hashlib import md5
from more_itertools import first_true

passcode = input()


def in_grid(p):
    return p.real in range(4) and p.imag in range(4)


def doors(path):
    seed = f'{passcode}{path}'.encode()
    h = md5(seed).hexdigest()[:4]
    return set('UDLR'[i] for i in range(4) if h[i] in 'bcdef')


def next_paths(paths):
    return {path + door
            for path in paths
            for door in doors(path)
            if in_grid(run(path + door))}


def run(path):
    steps = {'U': -1j, 'D': 1j, 'L': -1, 'R': 1}
    return sum(map(steps.get, path))


first, longest = '', 0

paths = ['']

while paths:
    paths = next_paths(paths)

    while 3+3j in map(run, paths):
        path = first_true(paths, pred=lambda p: run(p) == 3+3j)
        first = first or path
        longest = max(longest, len(path))
        paths.remove(path)

print(first, longest)
