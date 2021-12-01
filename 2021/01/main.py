# Parse data
ds = list(map(int, open(0).readlines()))

# Helper function
def increases(xs, ys):
    return sum([x2 > x1 for (x1, x2) in zip(xs, ys)])

# Part 1
print(increases(ds, ds[1:]))

# Part 2
print(increases(ds, ds[3:]))
