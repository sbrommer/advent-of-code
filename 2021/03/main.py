from collections import Counter


# Helper functions
def bin(x):
    return int(x, 2)


def count(xs):
    return T(Counter('10' + ''.join(xs)).most_common())[0]


def most_common(xs):
    return count(xs)[0]


def least_common(xs):
    return count(xs)[-1]


def T(xs):
    return list(zip(*xs))


def power_consumption(report, f):
    return bin(''.join(map(f, T(report))))


def life_support(report, f):
    report = report
    for i in range(len(report)):
        bit = f(T(report)[i])
        report = [x for x in report if x[i] == bit]
        if len(report) == 1:
            return bin(report[0])


# Parse
report = [line.strip() for line in open(0).readlines()]

# Part 1
gamma   = power_consumption(report, most_common)
epsilon = power_consumption(report, least_common)

print(gamma * epsilon)

# Part 2
oxygen = life_support(report, most_common)
co2    = life_support(report, least_common)

print(oxygen * co2)
