components = set(tuple(map(int, line.split('/')))
                 for line in open(0).readlines())


def get_bridges(t, bridges=[], current_bridge=[]):
    connecting = {c for c in components - set(current_bridge) if t in c}

    if not connecting:
        bridges += [current_bridge]
    else:
        for c in connecting:
            t_ = c[0] if c[1] == t else c[1]
            get_bridges(t_, bridges, current_bridge + [c])

    return bridges


def strength(bridges):
    def strength_(bridge): return sum(map(sum, bridge))
    return max(map(strength_, bridges))


def longest(bridges):
    l = max(map(len, bridges))
    return [b for b in bridges if len(b) == l]


bridges = get_bridges(0)
print(strength(bridges))
print(strength(longest(bridges)))
