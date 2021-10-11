from sys import stdin
from hashlib import md5

key = stdin.readline().strip()

def get_n(key, head):
    i = 0
    while True:
        n = key + str(i)
        hash = md5(n.encode('UTF-8')).hexdigest()

        if hash.startswith(head):
            return i

        i += 1

# part 1
print(get_n(key, '00000'))

# part 2
print(get_n(key, '000000'))
