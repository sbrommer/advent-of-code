from functools import cache

patterns, designs = open(0).read().strip().split('\n\n')

patterns = patterns.split(', ')
designs = designs.split()


def count(f, ps=patterns, ds=designs):
    @cache
    def count_(d):
        return not d or \
               f(count_(d.removeprefix(p))
                 for p in ps if d.startswith(p))

    return sum(map(count_, ds))


print(*map(count, [any, sum]))
