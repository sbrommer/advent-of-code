from collections import defaultdict

cat = ''.join


def parse(text=open(0)):
    return defaultdict(str) | \
           {(i, j): c for i, line in enumerate(text)
                      for j, c    in enumerate(line)}


wordsearch = parse()
keys = [*wordsearch.keys()]

print(sum(cat(wordsearch[(i+di*n, j+dj*n)] for n in range(4)) == 'XMAS'
          for di in [-1, 0, 1]
          for dj in [-1, 0, 1]
          for i, j in keys))

print(sum(cat(wordsearch[(i+n, j+n)] for n in [-1, 0, 1]) in {'MAS', 'SAM'} and
          cat(wordsearch[(i+n, j-n)] for n in [-1, 0, 1]) in {'MAS', 'SAM'}
          for i, j in keys))
