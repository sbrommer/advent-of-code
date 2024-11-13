def part1(n):
    b = format(n, 'b')
    w = b[1:] + '1'
    return int(w, 2)


def part2(n):
    i = 1
    while i * 3 < n:
        i *= 3

    if i < n <= 2 * i:
        w = n - i
    else:
        w = 2 * n - 3 * i

    return w


n = int(input())

print(part1(n))
print(part2(n))
