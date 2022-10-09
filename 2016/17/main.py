from hashlib import md5

passcode = 'qljzarfv'


def neighbours(x, y):
    ns = set()
    if y > 0: ns.add('U')
    if y < 3: ns.add('D')
    if x > 0: ns.add('L')
    if x < 3: ns.add('R')
    return ns


def doors(path):
    open_door = 'bcdef'
    seed = f'{passcode}{path}'.encode()
    h = md5(seed).hexdigest()[:4]

    doors = set()
    if h[0] in open_door: doors.add('U')
    if h[1] in open_door: doors.add('D')
    if h[2] in open_door: doors.add('L')
    if h[3] in open_door: doors.add('R')
    return doors


def moves(path):
    return neighbours(*run(path)) & doors(path)


def next_paths1(path):
    return set(path + move for move in moves(path))


def next_paths(paths):
    return set().union(*[next_paths1(path) for path in paths])


def run(path):
    x, y = 0, 0
    for step in path:
        if step == 'U': y -= 1
        if step == 'D': y += 1
        if step == 'L': x -= 1
        if step == 'R': x += 1
    return x, y


# Part 1
paths = ['']
while (3, 3) not in map(run, paths):
    paths = next_paths(paths)

print(next(p for p in paths if run(p) == (3, 3)))

# Part 2
longest = 0
paths = ['']
while paths:
    paths = next_paths(paths)

    while (3, 3) in map(run, paths):
        path = next(p for p in paths if run(p) == (3, 3))
        longest = max(longest, len(path))
        paths.remove(path)

print(longest)
