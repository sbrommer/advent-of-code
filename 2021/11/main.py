# Parse
energies = {(x, y): int(e) for y, l in enumerate(open(0))
                           for x, e in enumerate(l.strip())}


# Helper functions
def neighbours(x, y):
    neighbours = set((x + dx, y + dy)
                     for dx in [-1, 0, 1]
                     for dy in [-1, 0, 1]
                     if (dx, dy) != (0, 0))
    return neighbours & set(energies.keys())


def increase_and_get_flashing(octopusses):
    for octopus in octopusses:
        energies[octopus] += 1

    return {octopus for octopus in octopusses if energies[octopus] == 10}


# Calculate
step = 0
flashes = 0

while sum(energies.values()):
    # Step
    flashing = increase_and_get_flashing(energies)

    while flashing:
        flashes += 1
        octopus = flashing.pop()
        flashing |= increase_and_get_flashing(neighbours(*octopus))

    # Reset full energy
    for octopus, energy in energies.items():
        energies[octopus] *= energy < 10

    # Part 1
    if (step := step + 1) == 100:
        print(flashes)

# Part 2
print(step)
