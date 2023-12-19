from parse import parse
from re import findall
from math import prod
from itertools import starmap


# Parse
def parse_flows(flows):
    flows = dict(findall(r'(\w+){(.*)}', flows))

    def build_tree(s):
        if s in 'AR':
            return s == 'A'

        instr = s if ':' in s else flows[s]

        c, t, f = findall(r'([^:]*):([^,]*),(.*)', instr)[0]

        return c, build_tree(t), build_tree(f)

    return build_tree('in')


def parse_xmas(xmas):
    return [parse('{x={:d},m={:d},a={:d},s={:d}}', part)
            for part in xmas.split()]


flows, xmas = open(0).read().split('\n\n')
tree = parse_flows(flows)
xmas = parse_xmas(xmas)


# Part 1
def flow_one(x, m, a, s):
    def eval_(tree=tree):
        x, m, a, s  # otherwise eval doesn't acknowledge the existence of xmas

        if isinstance(tree, bool):
            return tree * (x + m + a + s)

        c, t, f = tree

        return eval_(t) if eval(c) else eval_(f)

    return eval_()


# Part 2
def flow_range(xmas, tree=tree):
    if isinstance(tree, bool):
        return tree * prod(e - s for s, e in xmas.values())

    c, t, f = tree

    v, o, n = findall(r'(\w+)(<|>)(.*)', c)[0]

    l, r = xmas[v]
    s = int(n) + (o == '>')
    p = [{v: (l, s)}, {v: (s, r)}]

    xmas_t = xmas | p[(o == '>')]
    xmas_f = xmas | p[(o == '<')]

    return flow_range(xmas_t, t) + flow_range(xmas_f, f)


print(sum(starmap(flow_one, xmas)),
      flow_range({v: (1, 4001) for v in 'xmas'}))
