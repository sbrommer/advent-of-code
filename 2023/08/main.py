from re import findall
from math import lcm

instr, network = open(0).read().split('\n\n')

network = findall(r'\w+', network)
network = dict(zip(network[::3], zip(network[1::3], network[2::3])))


def get_steps(node):
    s = 0
    while node[-1] != 'Z':
        node = network[node]['LR'.index(instr[s % len(instr)])]
        s += 1
    return s


nodes = filter(lambda n: n[-1] == 'A', network)

print(get_steps('AAA'), lcm(*map(get_steps, nodes)))
