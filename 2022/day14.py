import numpy as np

cave = np.zeros((1000, 200), dtype=int)
y_max = 0
with open("day14.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        rocks = [(int(s.split(",")[0]), int(s.split(",")[1])) for s in line.split(" -> ")]
        for r in range(len(rocks)-1):
            rock_start = rocks[r]
            rock_end = rocks[r+1]
            if rock_start[0] != rock_end[0]:
                lower = min(rock_start[0], rock_end[0])
                upper = max(rock_start[0], rock_end[0])
                for x in range(lower, upper+1):
                    cave[x, rock_start[1]] = -1
            elif rock_start[1] != rock_end[1]:
                lower = min(rock_start[1], rock_end[1])
                upper = max(rock_start[1], rock_end[1])
                for y in range(lower, upper+1):
                    cave[rock_start[0], y] = -1
                if y > y_max:
                    y_max = y

def simulate_pt1(c):
    overflowing = False
    while not overflowing:
        sand = (500, 0)
        rest = False
        while not rest:
            if sand[1] >= 180:
                overflowing = True
                break
            
            if c[sand[0], sand[1]+1] == 0:
                sand = (sand[0], sand[1]+1)
            elif c[sand[0]-1, sand[1]+1] == 0:
                sand = (sand[0]-1, sand[1]+1)
            elif c[sand[0]+1, sand[1]+1] == 0:
                sand = (sand[0]+1, sand[1]+1)
            else:
                c[sand] = 1
                rest = True
    return c


def simulate_pt2(c):
    overflowing = False
    while not overflowing:
        sand = (500, 0)
        rest = False
        while not rest:            
            if c[sand[0], sand[1]+1] == 0:
                sand = (sand[0], sand[1]+1)
            elif c[sand[0]-1, sand[1]+1] == 0:
                sand = (sand[0]-1, sand[1]+1)
            elif c[sand[0]+1, sand[1]+1] == 0:
                sand = (sand[0]+1, sand[1]+1)
            else:
                c[sand] = 1
                rest = True
            
            if sand == (500, 0):
                overflowing = True
                break

    return c

cave_filled = simulate_pt1(cave)
print("Units of sand resting:", sum(cave_filled[np.where(cave_filled == 1)]))

cave_floor = -np.ones(1000, dtype=int)
cave[:, y_max+2] += cave_floor
cave_filled = simulate_pt2(cave)
print("Units of sand resting:", sum(cave_filled[np.where(cave_filled == 1)]))

from matplotlib import pyplot as plt
plt.imshow(cave_filled.T)
plt.show()

