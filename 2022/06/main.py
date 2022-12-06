buffer = input()


def start_of_something(n):
    return [len(set(buffer[i:i+n])) for i in range(len(buffer))].index(n) + n


print(start_of_something(4))
print(start_of_something(14))
