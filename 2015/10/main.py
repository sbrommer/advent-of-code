from itertools import groupby


def apply_n(f, x, n):
    for i in range(n):
        x = f(x)
    return x


def look_and_say(x):
    return ''.join([str(len(list(g))) + n for n, g in groupby(x)])


x = input()
print(*[len(apply_n(look_and_say, x, n)) for n in [40, 50]])
