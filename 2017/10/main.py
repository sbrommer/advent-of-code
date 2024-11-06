from functools import reduce
from operator import xor


def hash(sequence, r=1):
    string = list(range(256))
    skip = 0
    d_pos = 0

    for _ in range(r):
        for i in sequence:
            # reverse
            string = string[:i][::-1] + string[i:]

            # move pos
            pos = (i+skip) % len(string)
            d_pos += pos
            string = string[pos:] + string[:pos]

            # update skip
            skip += 1

    pos = -(d_pos % len(string))  # original position 0
    return string[pos:] + string[:pos]


def dense_hash(hash):
    def xor_list(i): return reduce(xor, map(int, hash[i:i+16]))
    return map(xor_list, range(0, len(hash), 16))


def knot_hash(hash):
    def dec_to_hex(dec): return hex(dec).split('x')[-1].rjust(2, '0')
    return ''.join(map(dec_to_hex, hash))


inp = input()

# part 1
sequence = map(int, inp.split(','))
knot = hash(sequence)

print(knot[0] * knot[1])

# part 2
sequence = [ord(c) for c in inp] + [17, 31, 73, 47, 23]
sparce = hash(sequence, 64)
dense = dense_hash(sparce)
knot = knot_hash(dense)

print(knot)
