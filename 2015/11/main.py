from more_itertools import windowed, first_true
from itertools import count
from functools import reduce
from re import search


def is_valid(passnumber):
    password = base10to26(passnumber)

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    straight = set(windowed(alphabet, 3)) & set(windowed(password, 3))
    iol = search(r'[iol]', password)
    two_pair = search(r'(.)\1.*(.)\2', password)

    return straight and not iol and two_pair


def base10to26(passnumber):
    password = ''
    while passnumber:
        passnumber, o = divmod(passnumber, 26)
        password += chr(o + ord('a'))
    return password[::-1]


def base26to10(password):
    def f(passnumber, c):
        return passnumber * 26 + ord(c) - ord('a')

    return reduce(f, password, 0)


def next_password(password):
    passnumber = base26to10(password)
    passnumber = first_true(count(passnumber + 1), pred=is_valid)
    return base10to26(passnumber)


password = input()
print(password := next_password(password), next_password(password))
