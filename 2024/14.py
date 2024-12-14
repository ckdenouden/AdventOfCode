import math
import matplotlib.pyplot as plt
import numpy as np
import re


### Part 1
def move_robot(robot: dict) -> dict:
    robot["p"] = (
        (robot["p"][0] + robot["v"][0]) % FLOOR[0],
        (robot["p"][1] + robot["v"][1]) % FLOOR[1],
    )
    return robot


# Example
with open("2024/data/14_example.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

ROBOTS = []
for c in CONFIGURATION:
    robot = dict()
    match = re.search(r"p=(?P<p>-*\d+,-*\d+) v=(?P<v>-*\d+,-*\d+)", c)
    robot["p"] = tuple(int(i) for i in match.group("p").split(","))
    robot["v"] = tuple(int(i) for i in match.group("v").split(","))
    ROBOTS.append(robot)

FLOOR = (11, 7)
SECONDS = 100
for second in range(SECONDS):
    for idx, robot in enumerate(ROBOTS):
        ROBOTS[idx] = move_robot(robot)

QUADRANTS = {
    "pp": 0,
    "np": 0,
    "nn": 0,
    "pn": 0,
}
for robot in ROBOTS:
    # get x-quadrant
    if robot["p"][0] < FLOOR[0] // 2:
        quad_x = "n"
    elif robot["p"][0] > FLOOR[0] // 2:
        quad_x = "p"
    else:
        continue
    # get y-quadrant
    if robot["p"][1] < FLOOR[1] // 2:
        quad_y = "p"
    elif robot["p"][1] > FLOOR[1] // 2:
        quad_y = "n"
    else:
        continue
    QUADRANTS[quad_x + quad_y] += 1
print("Example 1:", math.prod(QUADRANTS.values()))

# Puzzle
with open("2024/data/14_input.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

ROBOTS = []
for c in CONFIGURATION:
    robot = dict()
    match = re.search(r"p=(?P<p>-*\d+,-*\d+) v=(?P<v>-*\d+,-*\d+)", c)
    robot["p"] = tuple(int(i) for i in match.group("p").split(","))
    robot["v"] = tuple(int(i) for i in match.group("v").split(","))
    ROBOTS.append(robot)

FLOOR = (101, 103)
SECONDS = 100
for second in range(SECONDS):
    for idx, robot in enumerate(ROBOTS):
        ROBOTS[idx] = move_robot(robot)

QUADRANTS = {
    "pp": 0,
    "np": 0,
    "nn": 0,
    "pn": 0,
}
for robot in ROBOTS:
    # get x-quadrant
    if robot["p"][0] < FLOOR[0] // 2:
        quad_x = "n"
    elif robot["p"][0] > FLOOR[0] // 2:
        quad_x = "p"
    else:
        continue
    # get y-quadrant
    if robot["p"][1] < FLOOR[1] // 2:
        quad_y = "p"
    elif robot["p"][1] > FLOOR[1] // 2:
        quad_y = "n"
    else:
        continue
    QUADRANTS[quad_x + quad_y] += 1
print("Puzzle 1:", math.prod(QUADRANTS.values()))

### Part 2
# Puzzle
with open("2024/data/14_input.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

ROBOTS = []
for c in CONFIGURATION:
    robot = dict()
    match = re.search(r"p=(?P<p>-*\d+,-*\d+) v=(?P<v>-*\d+,-*\d+)", c)
    robot["p"] = tuple(int(i) for i in match.group("p").split(","))
    robot["v"] = tuple(int(i) for i in match.group("v").split(","))
    ROBOTS.append(robot)

SECONDS = 8000
for second in range(SECONDS - 1000, SECONDS):
    for idx, robot in enumerate(ROBOTS):
        ROBOTS[idx] = move_robot(robot)

    floormap = np.zeros(FLOOR)
    for robot in ROBOTS:
        floormap[robot["p"]] = 1
    # plt.imsave(f"2024/day14/{second+1}.png", floormap.T, cmap="gray")
