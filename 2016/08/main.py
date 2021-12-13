# Imports
from parse import search


# Helper functions
def print_screen():
    for y in range(6):
        for x in range(50):
            print('#' if (x, y) in pixels else ' ', end='')
        print()


# Calculation
pixels = set()

for line in open(0).readlines():
    # Parse line
    line = line.strip()

    rct = search('{:d}x{:d}', line)
    col = search('x={:d} by {:d}', line)
    row = search('y={:d} by {:d}', line)

    # Add rectengles
    if rct:
        pixels |= {(x, y) for x in range(rct[0]) for y in range(rct[1])}

    # Shift column
    if col:
        old = {(x, y) for (x, y) in pixels if x == col[0]}

        pixels -= old
        pixels |= {(x, (y + col[1]) % 6) for (x, y) in old}

    # Shift row
    if row:
        old = {(x, y) for (x, y) in pixels if y == row[0]}

        pixels -= old
        pixels |= {((x + row[1]) % 50, y) for (x, y) in old}

# Part 1
print(len(pixels))

# Part 2
print_screen()
