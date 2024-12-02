from collections import defaultdict


def parse(text=open(0)):
    def parse_line(line): return tuple(map(int, line.split(', ')))
    return {*map(parse_line, text)}


def manhattan(p, q):
    return int(abs(p[0] - q[0]) + abs(p[1] - q[1]))


def closest(q, points):
    min_d = min(manhattan(p, q) for p in points)
    cs = [p for p in points if manhattan(p, q) == min_d]
    return None if len(cs) > 1 else cs[0]


def limits(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return map(int, [min(xs), max(xs), min(ys), max(ys)])


points = parse()
xmin, xmax, ymin, ymax = limits(points)

infinites = {closest((x, y), points)
             for x in range(xmin, xmax+1)
             for y in range(ymin, ymax+1)
             if x in [xmin, xmax] or y in [ymin, ymax] and
                closest((x, y), points)}

areas = defaultdict(int)
size = 0

for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        q = (x, y)
        c = closest(q, points)
        areas[c] += c not in infinites
        size += sum(manhattan(p, q) for p in points) < 10_000

print(max(areas.values()), size)
