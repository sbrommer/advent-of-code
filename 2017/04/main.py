def valid(passphrase):
    return len(passphrase) == len(set(passphrase))


def count_valid(passphrases):
    return sum(map(valid, passphrases))


passphrases1 = [line.split() for line in open(0).readlines()]
passphrases2 = [[''.join(sorted(word)) for word in passphrase] for passphrase in passphrases1]

print(count_valid(passphrases1), count_valid(passphrases2))
