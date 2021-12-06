from collections import defaultdict
from numpy import sign
from parse import findall

# Parse
results = list(findall('{:d},{:d} -> {:d},{:d}', open(0).read()))


# Helper functions
def my_range(a, b, l):
    d = sign(b - a)
    return [a + i * d for i in range(l + 1)]


# Actual calculation
for part in [0, 1]:
    counts = defaultdict(int)
    for x1, y1, x2, y2 in results:
        if part or x1 == x2 or y1 == y2:
            l = max(abs(x2 - x1), abs(y2 - y1))

            xs = my_range(x1, x2, l)
            ys = my_range(y1, y2, l)

            for p in zip(xs, ys):
                counts[p] += 1

    print(sum(v > 1 for v in counts.values()))
