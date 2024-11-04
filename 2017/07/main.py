def parse_input():
    W = {}
    G = {}

    for line in [line.strip() for line in open(0).readlines()]:
        children = []
        if '->' in line:
            line, children = line.split('->')
            children = [child.strip() for child in children.split(',')]

        name, weight = line.split()

        W[name] = int(weight[1:-1])
        G[name] = children

    return W, G


def get_root(G):
    for node in G:
        if not any(node in children for children in G.values()):
            return node


def total_weight(G, W, n):
    return W[n] + sum(total_weight(G, W, c) for c in G[n])


def get_unbalanced_child(G, W, n):
    weights = [total_weight(G, W, c) for c in G[n]]

    if len(set(weights)) <= 1:
        return None

    w, w_ = sorted(set(weights), key=weights.count, reverse=True)

    return G[n][weights.index(w_)], w - w_


def balance(G, W):
    n = get_root(G)

    while uc := get_unbalanced_child(G, W, n):
        n, dw = uc

    return W[n] + dw


W, G = parse_input()

print(get_root(G), balance(G, W))
