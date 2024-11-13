from operator import eq
from itertools import starmap


def next_row(row):
    return [*starmap(eq, zip([1] + row, row[1:] + [1]))]


def get_safe(row, n):
    safe = 0
    for _ in range(n):
        safe += sum(row)
        row = next_row(row)
    return safe


row = [tile == '.' for tile in input()]

print(get_safe(row, 40), get_safe(row, 400_000))
