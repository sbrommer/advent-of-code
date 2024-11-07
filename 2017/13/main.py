firewall = {int(depth): int(range_)
            for depth, range_ in [line.split(': ')
            for line in open(0).readlines()]}


def get_severity(t0=0):
    return sum([(t0+dt) * firewall[dt]
                for dt in firewall.keys()
                if not (t0+dt) % (firewall[dt] * 2 - 2)])


delay = 0
while get_severity(delay):
    delay += 1

print(get_severity(), delay)
