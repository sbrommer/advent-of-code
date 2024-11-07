# shameless copy-paste of day 10

from functools import reduce
from operator import xor


def reverse(string, i):
    return string[:i][::-1] + string[i:]


def move(string, pos):
    return string[pos:] + string[:pos]


def tie_string(sequence, r=1):
    string = list(range(256))
    skip = 0
    dpos = 0

    for _ in range(r):
        for i in sequence:
            pos = (i+skip) % len(string)

            string = reverse(string, i)
            string = move(string, pos)

            dpos += pos
            skip += 1

    pos = -(dpos % len(string))  # original position 0
    return move(string, pos)


def dense_hash(hash):
    def xor_list(i): return reduce(xor, map(int, hash[i:i+16]))
    return map(xor_list, range(0, len(hash), 16))


def hex_hash(hash):
    def dec_to_hex(dec): return hex(dec).split('x')[-1].rjust(2, '0')
    return ''.join(map(dec_to_hex, hash))


def knot_hash(string):
    sequence = [ord(c) for c in string] + [17, 31, 73, 47, 23]
    sparce = tie_string(sequence, 64)
    dense = dense_hash(sparce)
    return hex_hash(dense)


# actual day 14
def hex_to_bin(hex):
    return f'{int(hex, 16):0128b}'


key = input()

used = set()
for r in range(128):
    knot = knot_hash(f'{key}-{r}')
    bin_knot = hex_to_bin(knot)

    for c, b in enumerate(bin_knot):
        if int(b):
            used |= {complex(r, c)}


def DFS(u=0):
    visited = set()
    q = [u]

    while q:
        v = q.pop()
        visited |= {v}
        q += [v + dv for dv in [-1, 1, -1j, 1j]
              if v + dv in used and v + dv not in visited]

    return visited


vs = set(used)
n = 0
while vs:
    vs -= DFS(vs.pop())
    n += 1

print(len(used), n)
