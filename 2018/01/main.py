from itertools import accumulate

frequencies = accumulate


def repeat(changes):
    while True:
        yield from changes


def first_twice(xs):
    seen = set()

    for x in xs:
        if x in seen:
            return x
        seen |= {x}


changes = [int(n) for n in open(0)]

print(sum(changes), first_twice(frequencies(repeat(changes))))
