from hashlib import md5
from itertools import count

door_id = input()


def hash(i):
    return md5((door_id + str(i)).encode()).hexdigest()


def hashes():
    for h in map(hash, count()):
        if h.startswith('00000'):
            yield h


hs = hashes()

pw1 = ''
pw2 = [''] * 8

while not all(pw2):
    p, c = next(hs)[5:7]

    if len(pw1) < 8:
        pw1 += p

    try:
        p = int(p)
        if not pw2[p]:
            pw2[p] = c

    except (ValueError, IndexError):
        pass

print(pw1, ''.join(pw2))
