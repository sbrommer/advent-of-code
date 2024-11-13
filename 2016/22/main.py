def parse_line(line):
    node, *info = line.split()
    node = node.split('-')[-2:]

    x, y = tuple(map(lambda n: int(n[1:]), node))
    info = [*map(lambda i: int(i[:-1]), info)]

    return x+y*1j, info


nodes = dict(map(parse_line, [*open(0)][2:]))


# Part 1
def viable(k1, k2):
    return k1 != k2 and 0 < nodes[k1][1] <= nodes[k2][2]


pairs = [(k1, k2) for k1 in nodes for k2 in nodes if viable(k1, k2)]


# Part 2
# Kind of solved this by hand. Assume that the nodes with lots of data (>= 400)
# will never be used, and that all other nodes pairs are always viable.
# Now move the one node without any data to the goal data, taking the
# blocking nodes with lots of data in consideration. Then wiggle this empty node
# around the goal data to position (0, 0).

X = int(max(nodes, key=lambda node: node.real).real)
Y = int(max(nodes, key=lambda node: node.imag).imag)

p_empty = [p for p, info in nodes.items() if info[1] == 0][0]
ps_blocking = [p for p, info in nodes.items() if info[1] >= 400]
p_goal = X
p_00 = 0

# Print grid for visualisation.
for y in range(Y+1):
    for x in range(X+1):
        p = x+y*1j
        info = nodes[p]
        print('o' if p == p_empty else
              '*' if p == p_00 else
              'X' if p in ps_blocking else
              'G' if p == p_goal else
              '_', end='')
    print()

len_path = int(2 * (p_empty.real - min(p.real for p in ps_blocking) + 1) +
               p_empty.imag +
               p_goal.real - p_empty.real +
               5 * (X - 1))

print(len(pairs), len_path)
