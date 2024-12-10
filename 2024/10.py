### Part 1
global TRAILHEAD_ENDS_1
TRAILHEAD_ENDS_1 = set()


def get_trailheads(pos: tuple):
    directions = [
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1),
    ]

    valid_directions = [d for d in directions if 0 <= d[0] < len(TOPOGRAPHY) and 0 <= d[1] < len(TOPOGRAPHY[1])]

    for direction in valid_directions:
        if TOPOGRAPHY[direction[0]][direction[1]] == TOPOGRAPHY[pos[0]][pos[1]] + 1:
            if TOPOGRAPHY[direction[0]][direction[1]] == 9:
                TRAILHEAD_ENDS_1.add(direction)
            get_trailheads(direction)


# Example
with open("2024/data/10_example.txt", "r") as f:
    TOPOGRAPHY = f.readlines()
    TOPOGRAPHY = [[int(l2) if l2.isdigit() else -1 for l2 in l1.strip()] for l1 in TOPOGRAPHY]

TRAILHEADS = []
for row in range(len(TOPOGRAPHY)):
    TRAILHEADS_ROW = []
    for col in range(len(TOPOGRAPHY[row])):
        if TOPOGRAPHY[row][col] == 0:
            get_trailheads((row, col))
            TRAILHEADS_ROW.append(len(TRAILHEAD_ENDS_1))
        else:
            TRAILHEADS_ROW.append(0)
        TRAILHEAD_ENDS_1 = set()
    TRAILHEADS.append(TRAILHEADS_ROW)
print("Example 1:", sum(sum(TRAILHEADS, [])))

# Puzzle
with open("2024/data/10_input.txt", "r") as f:
    TOPOGRAPHY = f.readlines()
    TOPOGRAPHY = [[int(l2) if l2.isdigit() else -1 for l2 in l1.strip()] for l1 in TOPOGRAPHY]

TRAILHEADS = []
for row in range(len(TOPOGRAPHY)):
    TRAILHEADS_ROW = []
    for col in range(len(TOPOGRAPHY[row])):
        if TOPOGRAPHY[row][col] == 0:
            get_trailheads((row, col))
            TRAILHEADS_ROW.append(len(TRAILHEAD_ENDS_1))
        else:
            TRAILHEADS_ROW.append(0)
        TRAILHEAD_ENDS_1 = set()
    TRAILHEADS.append(TRAILHEADS_ROW)
print("Puzzle 1:", sum(sum(TRAILHEADS, [])))


### Part 2
global TRAILHEAD_ENDS_2
TRAILHEAD_ENDS_2 = list()


def get_trailheads(pos: tuple):
    directions = [
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1),
    ]

    valid_directions = [d for d in directions if 0 <= d[0] < len(TOPOGRAPHY) and 0 <= d[1] < len(TOPOGRAPHY[1])]

    for direction in valid_directions:
        if TOPOGRAPHY[direction[0]][direction[1]] == TOPOGRAPHY[pos[0]][pos[1]] + 1:
            if TOPOGRAPHY[direction[0]][direction[1]] == 9:
                TRAILHEAD_ENDS_2.append(direction)
            get_trailheads(direction)


# Example
with open("2024/data/10_example.txt", "r") as f:
    TOPOGRAPHY = f.readlines()
    TOPOGRAPHY = [[int(l2) if l2.isdigit() else -1 for l2 in l1.strip()] for l1 in TOPOGRAPHY]

TRAILHEADS = []
for row in range(len(TOPOGRAPHY)):
    TRAILHEADS_ROW = []
    for col in range(len(TOPOGRAPHY[row])):
        if TOPOGRAPHY[row][col] == 0:
            get_trailheads((row, col))
            TRAILHEADS_ROW.append(len(TRAILHEAD_ENDS_2))
        else:
            TRAILHEADS_ROW.append(0)
        TRAILHEAD_ENDS_2 = list()
    TRAILHEADS.append(TRAILHEADS_ROW)
print("Example 2:", sum(sum(TRAILHEADS, [])))

# Puzzle
with open("2024/data/10_input.txt", "r") as f:
    TOPOGRAPHY = f.readlines()
    TOPOGRAPHY = [[int(l2) if l2.isdigit() else -1 for l2 in l1.strip()] for l1 in TOPOGRAPHY]

TRAILHEADS = []
for row in range(len(TOPOGRAPHY)):
    TRAILHEADS_ROW = []
    for col in range(len(TOPOGRAPHY[row])):
        if TOPOGRAPHY[row][col] == 0:
            get_trailheads((row, col))
            TRAILHEADS_ROW.append(len(TRAILHEAD_ENDS_2))
        else:
            TRAILHEADS_ROW.append(0)
        TRAILHEAD_ENDS_2 = list()
    TRAILHEADS.append(TRAILHEADS_ROW)
print("Puzzle 2:", sum(sum(TRAILHEADS, [])))
