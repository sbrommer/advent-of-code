fav = int(input())


def is_space(p):
    x, y = map(int, [p.real, p.imag])
    n = x*x + 3*x + 2*x*y + y + y*y + fav
    return not bin(n).count('1') % 2


def neighbours(p):
    ps = [p + dp for dp in [-1, 1, -1j, 1j]]
    return {p for p in ps if p.real >= 0 and p.imag >= 0}


answer1, answer2 = 0, 0

# BFS
black, gray = set(), {1+1j}
i = 0

while not answer1 or not answer2:
    if 31+39j in gray:
        answer1 |= i
    if i == 51:
        answer2 |= len(black)

    i += 1
    black |= gray
    gray = {n for p in gray for n in neighbours(p)
            if is_space(n)} - black

print(answer1, answer2)
