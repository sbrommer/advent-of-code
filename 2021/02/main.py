from parse import search

h = a = d = 0

for line in open(0).readlines():
    # Parse line
    c, x = search('{:w} {:d}', line)

    # Compute values
    if c == 'forward':
        h += x
        d += a * x

    else:
        a += [-x, x][c == 'down']

# Part 1
print(h * a)

# Part 2
print(h * d)
