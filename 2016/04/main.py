# Imports
import re
from collections import Counter


# Helper functions
def get_checksum(name):
    counter = Counter(name).items()
    counter = sorted(counter, key=lambda t: t[0])
    counter = sorted(counter, key=lambda t: t[1], reverse=True)
    return ''.join(map(lambda t: t[0], counter))[:5]


def my_ord(c):
    return ord(c) - ord('a')


def my_chr(n):
    return chr(ord('a') + n)


def decrypt(name, id):
    def rotate(l):
        return ' ' if l == ' ' else my_chr((my_ord(l) + id) % 26)

    return ''.join(map(rotate, ' '.join(name)))


sum = 0
for line in open(0).readlines():
    # Parse line
    *name, id, checksum = re.findall(r'\w+', line)
    id = int(id)

    # Check if room is real
    if get_checksum(''.join(name)) == checksum:
        sum += id

        # Check if room is correct
        if decrypt(name, id) == 'northpole object storage':
            nos = id

print(sum)
print(nos)
