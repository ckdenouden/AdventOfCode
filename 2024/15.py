import matplotlib.pyplot as plt
import numpy as np

# print like you're supposed to, numpy
np.set_printoptions(
    edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" % x)
)

MOVE2DELTA = {
    ">": np.array((0, 1)),
    "^": np.array((-1, 0)),
    "<": np.array((0, -1)),
    "v": np.array((1, 0)),
}


### Part 1
def move_if_valid(robot: np.ndarray, move: str):
    if move == ">":
        map_seq = MAP[robot[0], robot[1] + 1 :]
        map_seq = map_seq[: np.argwhere(map_seq == "#")[0][0] + 1]
        if "." in map_seq:
            MAP[robot[0], robot[1] + 1 + np.argwhere(map_seq == ".")[0][0]] = "O"
            MAP[robot[0], robot[1] + 1] = "."
            return True
    elif move == "^":
        map_seq = MAP[: robot[0], robot[1]][::-1]
        map_seq = map_seq[: np.argwhere(map_seq == "#")[0][0] + 1]
        if "." in map_seq:
            MAP[robot[0] - 1 - np.argwhere(map_seq == ".")[0][0], robot[1]] = "O"
            MAP[robot[0] - 1, robot[1]] = "."
            return True
    elif move == "<":
        map_seq = MAP[robot[0], : robot[1]][::-1]
        map_seq = map_seq[: np.argwhere(map_seq == "#")[0][0] + 1]
        if "." in map_seq:
            MAP[robot[0], robot[1] - 1 - np.argwhere(map_seq == ".")[0][0]] = "O"
            MAP[robot[0], robot[1] - 1] = "."
            return True
    elif move == "v":
        map_seq = MAP[robot[0] + 1 :, robot[1]]
        map_seq = map_seq[: np.argwhere(map_seq == "#")[0][0] + 1]
        if "." in map_seq:
            MAP[robot[0] + 1 + np.argwhere(map_seq == ".")[0][0], robot[1]] = "O"
            MAP[robot[0] + 1, robot[1]] = "."
            return True
    return False


# Example
with open("2024/data/15_example.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

    MAP, MOVES = [], ""
    filling_map = True
    for idx, line in enumerate(CONFIGURATION):
        if filling_map:
            MAP.append(line)
        else:
            MOVES += line

        if idx != 0 and set(line) == set("#"):
            filling_map = False
MAP = np.array([[np.array(m2) for m2 in m1] for m1 in MAP])
ROBOT = np.array(np.argwhere(MAP == "@")[0])
MAP[*ROBOT] = "."

for move in MOVES:
    move_delta = MOVE2DELTA[move]
    robot_delta = ROBOT + move_delta
    map_delta = MAP[robot_delta[0]][robot_delta[1]]
    if map_delta == "." or (map_delta == "O" and move_if_valid(ROBOT, move)):
        ROBOT = robot_delta

GPS_SUM = 0
for box in np.argwhere(MAP == "O"):
    GPS_SUM += 100 * box[0] + box[1]
print("Example 1:", GPS_SUM)


# Puzzle
with open("2024/data/15_input.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

    MAP, MOVES = [], ""
    filling_map = True
    for idx, line in enumerate(CONFIGURATION):
        if filling_map:
            MAP.append(line)
        else:
            MOVES += line

        if idx != 0 and set(line) == set("#"):
            filling_map = False
MAP = np.array([[np.array(m2) for m2 in m1] for m1 in MAP])
ROBOT = np.array(np.argwhere(MAP == "@")[0])
MAP[*ROBOT] = "."

for move in MOVES:
    move_delta = MOVE2DELTA[move]
    robot_delta = ROBOT + move_delta
    map_delta = MAP[robot_delta[0]][robot_delta[1]]
    if map_delta == "." or (map_delta == "O" and move_if_valid(ROBOT, move)):
        ROBOT = robot_delta

GPS_SUM = 0
for box in np.argwhere(MAP == "O"):
    GPS_SUM += 100 * box[0] + box[1]
print("Puzzle 1:", GPS_SUM)


### Part 2
def deduplicate_lists(nested_lists):
    seen = set()
    result = []
    for sub in nested_lists:
        sorted_sub = tuple(sorted(sub))
        if sorted_sub not in seen:
            seen.add(sorted_sub)
            result.append(sub)
    return result


global INSTRUCTIONS
INSTRUCTIONS = []


def move_box_if_valid(robot: np.ndarray, move: str):
    if move == "^":
        offset = -1
    elif move == "v":
        offset = 1

    if MAP[robot[0] + offset][robot[1]] == "[":
        box = [
            np.array((robot[0] + offset, robot[1])),
            np.array((robot[0] + offset, robot[1] + 1)),
        ]
    else:
        box = [
            np.array((robot[0] + offset, robot[1])),
            np.array((robot[0] + offset, robot[1] - 1)),
        ]
    box_over = [np.array((b[0] + offset, b[1])) for b in box]

    ALIGNED = MAP[*box[0]] == MAP[*box_over[0]]
    if any(MAP[*b] == "#" for b in box_over):
        return False
    elif (
        all(MAP[*b] == "." for b in box_over)
        or (ALIGNED and move_box_if_valid(box[0], move))
        or (
            not ALIGNED
            and all(
                move_box_if_valid(b, move)
                for i, b in enumerate(box)
                if MAP[*box_over[i]] != "."
            )
        )
    ):
        INSTRUCTIONS.append(
            [
                f"MAP[{box_over[0][0]}][{box_over[0][1]}] = MAP[{box[0][0]}][{box[0][1]}]",
                f"MAP[{box_over[1][0]}][{box_over[1][1]}] = MAP[{box[1][0]}][{box[1][1]}]",
                f"MAP[{box[0][0]}][{box[0][1]}] = '.'",
                f"MAP[{box[1][0]}][{box[1][1]}] = '.'",
            ]
        )
        return True
    return False


def move_if_valid_wide(robot: np.ndarray, move: str):
    if move == ">":
        map_seq = MAP[robot[0], robot[1] + 1 :]
        map_seq = map_seq[: np.argwhere(map_seq == "#")[0][0] + 1]
        if "." in map_seq:
            newbox = robot[1] + 1 + np.argwhere(map_seq == ".")[0][0]
            MAP[robot[0], newbox] = "["
            MAP[robot[0], robot[1] + 1] = "."
            MAP[robot[0], robot[1] + 1 : newbox + 1] = np.char.replace(
                MAP[robot[0], robot[1] + 1 : newbox + 1], "[", "x"
            )
            MAP[robot[0], robot[1] + 1 : newbox + 1] = np.char.replace(
                MAP[robot[0], robot[1] + 1 : newbox + 1], "]", "["
            )
            MAP[robot[0], robot[1] + 1 : newbox + 1] = np.char.replace(
                MAP[robot[0], robot[1] + 1 : newbox + 1], "x", "]"
            )
            return True
    elif move == "<":
        map_seq = MAP[robot[0], : robot[1]][::-1]
        map_seq = map_seq[: np.argwhere(map_seq == "#")[0][0] + 1]
        map_seq = np.char.replace(map_seq, "[", "x")
        map_seq = np.char.replace(map_seq, "]", "[")
        map_seq = np.char.replace(map_seq, "x", "]")
        if "." in map_seq:
            newbox = robot[1] - 1 - np.argwhere(map_seq == ".")[0][0]
            MAP[robot[0], newbox] = "]"
            MAP[robot[0], robot[1] - 1] = "."
            MAP[robot[0], newbox : robot[1]] = np.char.replace(
                MAP[robot[0], newbox : robot[1]], "[", "x"
            )
            MAP[robot[0], newbox : robot[1]] = np.char.replace(
                MAP[robot[0], newbox : robot[1]], "]", "["
            )
            MAP[robot[0], newbox : robot[1]] = np.char.replace(
                MAP[robot[0], newbox : robot[1]], "x", "]"
            )
            return True
    elif move in ["^", "v"] and move_box_if_valid(robot, move):
        for i, instruction in enumerate(sum(deduplicate_lists(INSTRUCTIONS), [])):
            exec(instruction)
        return True
    return False


# Example
with open("2024/data/15_example.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

    MAP, MOVES = [], ""
    filling_map = True
    for idx, line in enumerate(CONFIGURATION):
        if filling_map:
            MAP.append(
                line.replace("#", "##")
                .replace("O", "[]")
                .replace(".", "..")
                .replace("@", "@.")
            )

        else:
            MOVES += line

        if idx != 0 and set(line) == set("#"):
            filling_map = False
MAP = np.array([[np.array(m2) for m2 in m1] for m1 in MAP])
ROBOT = np.array(np.argwhere(MAP == "@")[0])
MAP[*ROBOT] = "."

for move in MOVES:
    INSTRUCTIONS = []
    move_delta = MOVE2DELTA[move]
    robot_delta = ROBOT + move_delta
    map_delta = MAP[robot_delta[0]][robot_delta[1]]
    if map_delta == "." or (
        map_delta in ["[", "]"] and move_if_valid_wide(ROBOT, move)
    ):
        ROBOT = robot_delta

GPS_SUM = 0
for box in np.argwhere(MAP == "["):
    GPS_SUM += 100 * box[0] + box[1]
print("Example 2:", GPS_SUM)

# Puzzle
with open("2024/data/15_input.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

    MAP, MOVES = [], ""
    filling_map = True
    for idx, line in enumerate(CONFIGURATION):
        if filling_map:
            MAP.append(
                line.replace("#", "##")
                .replace("O", "[]")
                .replace(".", "..")
                .replace("@", "@.")
            )

        else:
            MOVES += line

        if idx != 0 and set(line) == set("#"):
            filling_map = False
MAP = np.array([[np.array(m2) for m2 in m1] for m1 in MAP])
ROBOT = np.array(np.argwhere(MAP == "@")[0])
MAP[*ROBOT] = "."

for i, move in enumerate(MOVES):
    INSTRUCTIONS = []
    move_delta = MOVE2DELTA[move]
    robot_delta = ROBOT + move_delta
    map_delta = MAP[robot_delta[0]][robot_delta[1]]
    if map_delta == "." or (
        map_delta in ["[", "]"] and move_if_valid_wide(ROBOT, move)
    ):
        ROBOT = robot_delta

GPS_SUM = 0
for box in np.argwhere(MAP == "["):
    GPS_SUM += 100 * box[0] + box[1]
print("Puzzle 2:", GPS_SUM)
