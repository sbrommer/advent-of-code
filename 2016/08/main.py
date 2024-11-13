from parse import search


def print_screen(pixels):
    for y in range(6):
        for x in range(50):
            print('#' if (x, y) in pixels else ' ', end='')
        print()


pixels = set()

for line in [line.strip() for line in open(0)]:
    rct = search('{:d}x{:d}', line)
    col = search('x={:d} by {:d}', line)
    row = search('y={:d} by {:d}', line)

    # Add rectangles
    if rct:
        pixels |= {(x, y) for x in range(rct[0]) for y in range(rct[1])}

    # Shift column
    if col:
        prev = {(x, y) for x, y in pixels if x == col[0]}

        pixels -= prev
        pixels |= {(x, (y + col[1]) % 6) for x, y in prev}

    # Shift row
    if row:
        prev = {(x, y) for x, y in pixels if y == row[0]}

        pixels -= prev
        pixels |= {((x + row[1]) % 50, y) for x, y in prev}


print(len(pixels))
print_screen(pixels)
