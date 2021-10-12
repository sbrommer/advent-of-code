from sys import stdin
from re import search

lines = stdin.readlines()

# part 1
def is_nice(line):
    return search(r'(.*[aeiou]){3,}', line) and \
           search(r'(.)\1', line) and \
           not search(r'ab|cd|pq|xy', line)

print(sum([bool(is_nice(line)) for line in lines]))

# part 2
def is_really_nice(line):
    return search(r'(..).*\1', line) and \
           search(r'(.).\1', line)

print(sum([bool(is_really_nice(line)) for line in lines]))
