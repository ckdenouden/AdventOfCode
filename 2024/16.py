import numpy as np

MAZE2NUM = {".": 0, "#": 2, "E": "E", "S": "S"}


### Part 1
def get_options(pos: np.ndarray, traversed: list):
    options = [
        pos + np.array((0, 1)),
        pos + np.array((1, 0)),
        pos + np.array((0, -1)),
        pos + np.array((-1, 0)),
    ]
    return [option for option in options if MAP[*option] == 0 and option not in traversed]

def traverse(pos: np.ndarray):

    


# Example
with open("2024/data/16_example.txt", "r") as f:
    MAP = f.readlines()
    MAP = [[MAZE2NUM[l2] for l2 in l1.strip()] for l1 in MAP]
MAP = np.array([[np.array(m2) for m2 in m1] for m1 in MAP])
START = np.array(np.argwhere(MAP == "S")[0])
END = np.array(np.argwhere(MAP == "E")[0])
MAP[*START] = 0
MAP[*END] = 0
MAP = MAP.astype(int)

print(START)
print(MAP)


print(get_options(START, []))


# Puzzle


### Part 2
# Example

# Puzzle
