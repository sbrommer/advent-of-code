from hashlib import md5
from itertools import count
from more_itertools import first_true


def hash(key, i):
    return md5((key + str(i)).encode('UTF-8')).hexdigest()


def n(key, head):
    return first_true(count(),
                      pred=lambda i: hash(key, i).startswith(head))


key = input()
print(*[n(key, '0' * z) for z in [5, 6]])
