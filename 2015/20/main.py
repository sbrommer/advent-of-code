import numpy as np

# Parse
n = int(open(0).readline())

# Calculate both parts
presents = np.zeros((2, n // 10))
for e in range(1, n // 10):
    presents[0, e::e] += 10 * e
    presents[1, e:(50*e)+1:e] += 11 * e

# Part 1
print(np.where(presents[0,:] >= n)[0][0])

# Part 2
print(np.where(presents[1,:] >= n)[0][0])
