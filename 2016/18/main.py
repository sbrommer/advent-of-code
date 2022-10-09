def parse_row(row):
    return [tile == '.' for tile in row]


def next_row(row):
    row = [True] + row + [True]
    return [row[i] == row[i+2] for i in range(len(row)-2)]


rows = [parse_row(open(0).readline().strip())]

for _ in range(40-1):
    rows.append(next_row(rows[-1]))

print(sum(row.count(True) for row in rows))
