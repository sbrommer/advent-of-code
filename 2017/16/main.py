def dance(order, moves):
    def swap(a, b):
        order[a], order[b] = order[b], order[a]

    order = [c for c in order]

    for move in moves:
        type, args = move[0], move[1:].split('/')

        match type:
            case 's':
                n = int(args[0])
                order = order[-n:] + order[:-n]

            case 'x':
                swap(*map(int, args))

            case 'p':
                swap(*map(order.index, args))

    return ''.join(order)


moves = input().split(',')
start = 'abcdefghijklmnop'

# determine cycle
order = start
cycle = 0
while not cycle or order != start:
    order = dance(order, moves)
    cycle += 1

# do last dances
order = start
for _ in range(1_000_000_000 % cycle):
    order = dance(order, moves)

print(dance(start, moves), order)
