from itertools import accumulate


def move(p):
    return 1 if p == '(' else -1


instructions = input()
floors = [*accumulate(map(move, instructions))]

print(floors[-1], 1 + floors.index(-1))
