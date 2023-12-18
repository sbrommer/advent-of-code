lights = {complex(x, y)
          for y, l in enumerate(open(0))
          for x, c in enumerate(l)
          if c == '#'}


bulbs = {complex(x, y) for x in range(100) for y in range(100)}
corners = {0, 99j, 99, 99 + 99j}


def neighbours(light):
    return {light + d for d in [-1-1j, -1, -1+1j, -1j, 1j, 1-1j, 1, 1+1j]}


def solve(lights, corners={}):
    def new_state(bulb):
        n = len(neighbours(bulb) & lights)
        return any([bulb in lights and n == 2, n == 3, bulb in corners])

    for i in range(100):
        lights = set(filter(new_state, bulbs))

    return len(lights)


print(solve(lights),
      solve(lights | corners, corners))
