# Helper functions
def taxicab(x):
    return int(abs(x.real) + abs(x.imag))


# Constants
rotations = {'R': -1j, 'L': +1j}

# Calculate locations
## Initalise
dir = 1j
loc = 0j
seen = {loc}
hq = None

## Walk
for i in input().split(', '):
    dir *= rotations[i[0]]

    for b in range(int(i[1:])):
        loc += dir
        if hq is None:
            if loc in seen:
                hq = loc
            seen.add(loc)

# Result
print(*map(taxicab, [loc, hq]))
