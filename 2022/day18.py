import numpy as np


coordinates = []
gridsize = 25
grid = np.zeros((gridsize, gridsize, gridsize), dtype=int)
with open("day18.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        coordinate = tuple([int(c) for c in line.split(",")])
        coordinates.append(coordinate)
        grid[coordinate] = 1


def get_adjacent(coordinate):
    x, y, z = coordinate

    left = (x-1, y, z)
    right = (x+1, y, z)
    back = (x, y+1, z)
    front = (x, y-1, z)
    up = (x, y, z+1)
    down = (x, y, z-1)
    return [left, right, back, front, up, down]


surface_area = 0
for c in coordinates:
    adjacent = get_adjacent(c)
    for a in adjacent:
        if not grid[a]:
            surface_area += 1
print(surface_area)

outside = {(0, 0, 0)}
for _ in range(5):
    for z in range(-1, gridsize):
        for y in range(-1, gridsize):
            for x in range(-1, gridsize):
                isopen = False
                adjacent = get_adjacent((x, y, z))
                adjacent = [a for a in adjacent if -2 not in a and gridsize+1 not in a]
                for a in adjacent:
                    if a not in coordinates and a in outside:
                        isopen = True
                if isopen:
                    outside.add((x, y, z))

surface_area = 0
shell = []
for c in coordinates:
    adjacent = get_adjacent(c)
    for a in adjacent:
        if not grid[a] and a in outside:
            shell.append(a)
            surface_area += 1
print(surface_area)