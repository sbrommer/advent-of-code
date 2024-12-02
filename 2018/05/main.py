cat = ''.join

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = alphabet.upper()
reactions = [*zip(alphabet, ALPHABET)] + [*zip(ALPHABET, alphabet)]


def react(polymer):
    for a, A in reactions:
        polymer = polymer.replace(a+A, '')

    return polymer


def converge(polymer):
    while (new := react(polymer)) != polymer:
        polymer = new
    return len(polymer)


def improve(polymer, a):
    return polymer.replace(a, '').replace(a.upper(), '')


polymer = cat(input())

converged = converge(polymer)
improved = min(converge(improve(polymer, a)) for a in alphabet)

print(converged, improved)
