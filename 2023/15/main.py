from re import split
from functools import reduce


def hash(string):
    def f(value, char):
        return ((value + ord(char)) * 17) % 256
    return reduce(f, string, 0)


def initialise(sequence):
    boxes = [{} for _ in range(256)]

    for operation in sequence:
        label, focal_length = split(r'=|-', operation)
        box = boxes[hash(label)]

        if focal_length:
            box[label] = focal_length
        else:
            box.pop(label, 0)

    return boxes


def power(boxes):
    return sum(b * slot * int(focal_length)
               for b, box in enumerate(boxes, 1)
               for slot, focal_length in enumerate(box.values(), 1))


sequence = open(0).read().strip().split(',')

print(sum(map(hash, sequence)),
      power(initialise(sequence)))
