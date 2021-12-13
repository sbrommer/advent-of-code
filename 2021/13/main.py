from parse import findall

# Parse
instr = open(0).read()
dots  = findall('{:d},{:d}', instr)
folds = findall('{:w}={:d}', instr)

# Fold
first = True
for a, n in folds:
    dots = {(x if (a == 'y' or x <= n) else (2 * n - x),
             y if (a == 'x' or y <= n) else (2 * n - y))
             for (x, y) in dots}

    # Part 1
    if first:
        print(len(dots))
        first = False

# Part 2

X, Y = map(max, zip(*dots))

for y in range(Y + 1):
    for x in range(X + 1):
        print('#' if (x, y) in dots else ' ', end='')
    print()
