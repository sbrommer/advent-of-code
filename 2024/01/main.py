def transpose(xs): return zip(*xs)


def parse(text=open(0)):
    def parse_line(line): return map(int, line.split())

    return [*map(sorted, transpose(map(parse_line, text)))]


def distance(lists):
    return sum(map(lambda x, y: abs(x - y), *lists))


def similarity(l1, l2):
    return sum(n * l2.count(n) for n in l1)


lists = parse()
print(distance(lists), similarity(*lists))
