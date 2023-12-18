import numpy as np

n = int(open(0).readline())

presents = np.zeros((2, n // 10))
for elf in range(1, n // 10):
    presents[0, elf::elf] += 10 * elf
    presents[1, elf:(50*elf)+1:elf] += 11 * elf

# Part 1
print(np.where(presents[0,:] >= n)[0][0])

# Part 2
print(np.where(presents[1,:] >= n)[0][0])
