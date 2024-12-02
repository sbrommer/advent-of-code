import re
from datetime import datetime
from collections import defaultdict
from heapq import heappop, heapify


def parse(text=open(0)):
    q = [*map(parse_line, text)]
    heapify(q)
    return q


def parse_line(line):
    m = r'\[(.+)\] (.+)'
    dt, event = re.findall(m, line)[0]
    dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')
    return dt, event


def q_to_dict(q):
    guards = defaultdict(lambda: defaultdict(int))
    g, t = -1, None

    while q:
        dt, event = heappop(q)
        match event:
            case 'falls asleep':
                t = dt.minute
            case 'wakes up':
                for m in range(t, dt.minute):
                    guards[g][m] += 1
            case _:
                g = int(re.search(r'\d+', event).group())

    return guards


def sleepiest(guards, f):
    g, minutes = max(guards.items(), key=lambda kv: f(kv[1].values()))
    return g * max(minutes, key=minutes.get)


q = parse()
guards = q_to_dict(q)

print(*[sleepiest(guards, f) for f in [sum, max]])
