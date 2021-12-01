import re
import json


# Helper functions
def sum_of_digits(s):
    return sum(map(int, re.findall(r'\-?\d+', s)))


def remove_red(o):
    if isinstance(o, dict):
        if 'red' in o.values():
            o.clear()

        for v in o.values():
            remove_red(v)

    if isinstance(o, list):
        for v in o:
            remove_red(v)


# Read data
s = open(0).readline()

# Part 1
print(sum_of_digits(s))

# Part 2
j = json.loads(s)
remove_red(j)
print(sum_of_digits(str(j)))
