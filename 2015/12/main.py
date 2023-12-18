from re import findall
import json


def sum_of_digits(s):
    return sum(map(int, findall(r'\-?\d+', s)))


def remove_red(o):
    if isinstance(o, dict):
        if 'red' in o.values():
            o.clear()

        for v in o.values():
            remove_red(v)

    if isinstance(o, list):
        for v in o:
            remove_red(v)


document = input()

# Part 1
print(sum_of_digits(document))

# Part 2
json_ = json.loads(document)
remove_red(json_)
print(sum_of_digits(str(json_)))
