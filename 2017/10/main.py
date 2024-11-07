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


inp = input()

# part 1
sequence = map(int, inp.split(','))
tied_string = tie_string(sequence)

print(tied_string[0] * tied_string[1])

# part 2
print(knot_hash(inp))
