from dataclasses import dataclass, field
from math import prod
import re


@dataclass
class Module:
    label: str
    children: list = field(default_factory=list)
    status: int = 0
    memory: dict = field(default_factory=dict)

    def __hash__(self):
        return id(self.label)

    def __repr__(self):
        return self.label

    def process(self, source, pulse):
        if isinstance(self, Flipflop) and pulse:
            return []

        self.process_(source, pulse)
        return [(self, self.status, child) for child in self.children]


class End(Module):
    def process_(self, source, pulse):
        self.status = pulse


class Flipflop(Module):
    def process_(self, source, pulse):
        self.status = not self.status


class Conjunction(Module):
    def process_(self, source, pulse):
        self.memory[source] = pulse
        self.status = not all(self.memory.values())


# Parse
def parse_module(line):
    t, label, children = re.findall(r'([%&]?)(\w+) -> (.*)', line)[0]
    types = {'': End, '%': Flipflop, '&': Conjunction}
    return label, types[t](label, children.split(', '))


modules = dict(map(parse_module, open(0)))

for module in modules.values():
    module.children = [modules.get(c, End(c)) for c in module.children]

    for child in module.children:
        child.memory[module] = 0

# Run
i = -1
n = [0, 0]
cycles = {m: None for m in modules.get('qb', Module('qb')).memory}

while (i := i+1) <= 1000 or not all(cycles.values()):
    pulses = [(None, False, modules['broadcaster'])]

    while pulses:
        source, pulse, dest = pulses.pop()
        pulses += dest.process(source, pulse)
        n[pulse] += i < 1000

        if dest in cycles and not cycles[dest] and dest.status:
            cycles[dest] = i

print(prod(n), prod(cycles.values()))
