from itertools import product


def checksum1(row):
    return max(row) - min(row)


def checksum2(row):
    for i, j in product(row, row):
        if i != j and not j % i:
            return j // i


spreadsheet = [[int(i) for i in line.split()]
               for line in open(0).readlines()]

print(sum(map(checksum1, spreadsheet)),
      sum(map(checksum2, spreadsheet)))
