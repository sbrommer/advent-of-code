from re import search

strings = [*open(0)]


def is_nice(string):
    return bool(search(r'(.*[aeiou]){3,}', string) and
                search(r'(.)\1', string) and
                not search(r'ab|cd|pq|xy', string))


def is_really_nice(string):
    return bool(search(r'(..).*\1', string) and
                search(r'(.).\1', string))


print(sum(map(is_nice, strings)),
      sum(map(is_really_nice, strings)))
