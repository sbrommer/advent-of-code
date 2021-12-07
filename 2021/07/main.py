from numpy import *

# Parse
cs = fromfile(open(0), int, sep=',')
cs = cs.reshape((1000, 1))

# Part 1
print(int(sum(abs(cs - median(cs)))))


# Part 2
def fuel(xs):
    return multiply(xs, xs + 1) / 2


m = matrix([floor(mean(cs)), ceil(mean(cs))])

print(int(fuel(abs(cs - m)).sum(0).min(1)[0]))
