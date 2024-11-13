from collections import Counter
from more_itertools import first_true


def parse_line(line):
    *name, i, checksum = line.replace('[', '-').replace(']\n', '').split('-')
    return {'name': ''.join(name), 'id': int(i), 'checksum': checksum}


def check(room):
    counter = Counter(room['name'])
    sorted_ = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
    checksum = ''.join(t[0] for t in sorted_[:5])
    return checksum == room['checksum']


def is_storage(room):
    def decrypt(c):
        return chr(97 + (ord(c) + room['id'] - 97) % 26)

    name = ''.join(map(decrypt, room['name']))

    return name == 'northpoleobjectstorage'


rooms = [*map(parse_line, open(0))]
reals = [*filter(check, rooms)]

print(sum(room['id'] for room in reals),
      first_true(rooms, pred=is_storage)['id'])
