from more_itertools import windowed
import re

# Helper functions
def increase_char(c):
    d = chr(ord(c) + 1)
    return d if d <= 'z' else 'a'

def increase_i(pw, i):
    pw[i] = increase_char(pw[i])
    while pw[i] == 'a':
        i -= 1
        pw[i] = increase_char(pw[i])

    return pw

def increase(pw):
    return ''.join(increase_i(list(pw), -1))

def straight(pw):
    for w in windowed(pw, 3):
        w = list(map(ord, w))
        if w[0] + 1 == w[1] and w[1] + 1 == w[2]:
           return True

    return False

def iol(pw):
    return re.search(r'[iol]', pw)

def two_pair(pw):
    return re.search(r'(.)\1.*(.)\2', pw)

def is_valid(pw):
    return straight(pw) and not iol(pw) and two_pair(pw)

# Read data
pw = open(0).readline().strip()

# # Part 1
while not is_valid(pw):
    pw = increase(pw)
print(pw)

# # Part 2
pw = increase(pw)
while not is_valid(pw):
    pw = increase(pw)
print(pw)
