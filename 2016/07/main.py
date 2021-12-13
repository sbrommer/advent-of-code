# Imports
import re
from itertools import chain

# Read data
lines = open(0).readlines()


# Helper functions
def abba(x):
    return x[0] == x[3] and x[1] == x[2] and x[0] != x[1]


def get_abbas(xs):
    slices = [xs[i:i+4] for i in range(len(xs) - 3)]
    return list(filter(abba, slices))


def aba(x):
    return x[0] == x[2] and x[0] != x[1]


def get_abas(xs):
    slices = [xs[i:i+3] for i in range(len(xs) - 2)]
    return list(filter(aba, slices))


def get_babs(xs):
    return [aba[1] + aba[0] + aba[1] for aba in get_abas(xs)]


# Calculation
tls = 0
ssl = 0
for line in lines:
    # Parse line
    parts = re.split('[\[\]]', line.strip())
    ips = parts[0::2]
    hns = parts[1::2]

    # Part 1
    ips_abbas = map(get_abbas, ips)
    hns_abbas = map(get_abbas, hns)

    tls += any(ips_abbas) and not any(hns_abbas)

    # Part 2
    ips_abas = set(chain(*map(get_abas, ips)))
    hns_babs = set(chain(*map(get_babs, hns)))

    ssl += len(ips_abas.intersection(hns_babs)) > 0

# Part 1
print(tls)

# Part 2
print(ssl)
