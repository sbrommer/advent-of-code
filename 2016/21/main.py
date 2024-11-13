from parse import search
from itertools import permutations


def scramble(password, lines):
    for line in lines:
        if args := search('swap position {:d} with position {:d}', line):
            password = swap_positions(password, *args)

        if args := search('swap letter {:w} with letter {:w}', line):
            password = swap_letters(password, *args)

        if args := search('rotate left {:d}', line):
            password = rotate_left(password, *args)

        if args := search('rotate right {:d}', line):
            password = rotate_right(password, *args)

        if args := search('rotate based on position of letter {:w}', line):
            password = rotate_position(password, *args)

        if args := search('reverse positions {:d} through {:d}', line):
            password = reverse(password, *args)

        if args := search('move position {:d} to position {:d}', line):
            password = move(password, *args)

    return ''.join(password)


def swap_positions(password, p, q):
    password[p], password[q] = password[q], password[p]
    return password


def swap_letters(password, a, b):
    p = password.index(a)
    q = password.index(b)
    return swap_positions(password, p, q)


def rotate_left(password, n):
    n %= len(password)
    return password[n:] + password[:n]


def rotate_right(password, n):
    n %= len(password)
    return password[-n:] + password[:-n]


def rotate_position(password, a):
    n = password.index(a)
    return rotate_right(password, 1 + n + int(n >= 4))


def reverse(password, p, q):
    password[p:q+1] = password[p:q+1][::-1]
    return password


def move(password, p, q):
    temp = password[p]
    del password[p]
    return password[:q] + [temp] + password[q:]


lines = open(0)

# part 1
password = list('abcdefgh')
print(scramble(password, lines))

# part 2

password = list('fbgdceah')
for p in permutations(password):
    if scramble(list(p), lines) == ''.join(password):
        print(''.join(p))
        break
