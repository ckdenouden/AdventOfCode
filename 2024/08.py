from itertools import combinations


def find_antinodes_p1(node_0: tuple, node_1: tuple) -> list[tuple]:
    delta = (node_0[0] - node_1[0], node_0[1] - node_1[1])
    antinodes = [
        (node_0[0] + delta[0], node_0[1] + delta[1]),
        (node_1[0] - delta[0], node_1[1] - delta[1]),
    ]
    return [a for a in antinodes if 0 <= a[0] <= BOUNDS[0] and 0 <= a[1] <= BOUNDS[1]]


def find_antinodes_p2(node_0: tuple, node_1: tuple) -> list[tuple]:
    delta = (node_0[0] - node_1[0], node_0[1] - node_1[1])
    antinodes = []

    # extend from 0 to 1
    antinode = node_0
    while 0 <= antinode[0] <= BOUNDS[0] and 0 <= antinode[1] <= BOUNDS[1]:
        antinodes.append(antinode)
        antinode = antinode[0] - delta[0], antinode[1] - delta[1]

    # extend from 1 to 0
    antinode = node_1
    while 0 <= antinode[0] <= BOUNDS[0] and 0 <= antinode[1] <= BOUNDS[1]:
        antinodes.append(antinode)
        antinode = antinode[0] + delta[0], antinode[1] + delta[1]

    return list(set(antinodes))


### Part 1
# Example
with open("2024/data/08_example.txt", "r") as f:
    mappie = f.readlines()
    mappie = [l.strip() for l in mappie]

antenna = dict()
for row, l in enumerate(mappie):
    for col, c in enumerate(l):
        BOUNDS = (row, col)
        if c != ".":
            if c not in antenna:
                antenna[c] = []
            antenna[c].append((row, col))

antinodes = dict()
for freq, nodes in antenna.items():
    if freq not in antinodes:
        antinodes[freq] = []
    for combination in combinations(nodes, 2):
        antinodes[freq] += find_antinodes_p1(combination[0], combination[1])
antinodes_unique = list(set(sum(antinodes.values(), [])))
print("Example 1:", len(antinodes_unique))

# Puzzle
with open("2024/data/08_input.txt", "r") as f:
    mappie = f.readlines()
    mappie = [l.strip() for l in mappie]

antenna = dict()
for row, l in enumerate(mappie):
    for col, c in enumerate(l):
        BOUNDS = (row, col)
        if c != ".":
            if c not in antenna:
                antenna[c] = []
            antenna[c].append((row, col))

antinodes = dict()
for freq, nodes in antenna.items():
    if freq not in antinodes:
        antinodes[freq] = []
    for combination in combinations(nodes, 2):
        antinodes[freq] += find_antinodes_p1(combination[0], combination[1])
antinodes_unique = list(set(sum(antinodes.values(), [])))
print("Puzzle 1:", len(antinodes_unique))

### Part 2
# Example
with open("2024/data/08_example.txt", "r") as f:
    mappie = f.readlines()
    mappie = [l.strip() for l in mappie]

antenna = dict()
for row, l in enumerate(mappie):
    for col, c in enumerate(l):
        BOUNDS = (row, col)
        if c != ".":
            if c not in antenna:
                antenna[c] = []
            antenna[c].append((row, col))

antinodes = dict()
for freq, nodes in antenna.items():
    if freq not in antinodes:
        antinodes[freq] = []
    for combination in combinations(nodes, 2):
        antinodes[freq] += find_antinodes_p2(combination[0], combination[1])
antinodes_unique = list(set(sum(antinodes.values(), [])))
print("Example 2:", len(antinodes_unique))

# Puzzle
with open("2024/data/08_input.txt", "r") as f:
    mappie = f.readlines()
    mappie = [l.strip() for l in mappie]

antenna = dict()
for row, l in enumerate(mappie):
    for col, c in enumerate(l):
        BOUNDS = (row, col)
        if c != ".":
            if c not in antenna:
                antenna[c] = []
            antenna[c].append((row, col))

antinodes = dict()
for freq, nodes in antenna.items():
    if freq not in antinodes:
        antinodes[freq] = []
    for combination in combinations(nodes, 2):
        antinodes[freq] += find_antinodes_p2(combination[0], combination[1])
antinodes_unique = list(set(sum(antinodes.values(), [])))
print("Puzzle 2:", len(antinodes_unique))
