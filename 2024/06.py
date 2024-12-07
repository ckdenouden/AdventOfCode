import numpy as np

### Part 1
step = {
    "N": np.asarray([-1, 0]),
    "E": np.asarray([0, 1]),
    "S": np.asarray([1, 0]),
    "W": np.asarray([0, -1]),
}
step_keys = list(step.keys())

# Example
with open("2024/data/06_example.txt", "r") as f:
    mappie = f.readlines()
    mappie = [[l2 for l2 in l1.strip()] for l1 in mappie]

# preprocess mappie
mappie_numeric = []
for row_idx, row in enumerate(mappie):
    mappie_numeric_row = []
    for cell_idx, cell in enumerate(row):
        if cell == "#":
            mappie_numeric_row.append(-1)
        elif cell == "^":
            guard = [np.asarray([row_idx + 1, cell_idx + 1]), "N"]
            mappie_numeric_row.append(0)
        else:
            mappie_numeric_row.append(0)
    mappie_numeric.append(np.asarray(mappie_numeric_row))
mappie_np = np.pad(np.asarray(mappie_numeric), pad_width=1, constant_values=-2)

# walk the guard
while True:
    mappie_np[*guard[0]] = 1
    guard_new = guard[0] + step[guard[1]]
    if mappie_np[*guard_new] == -1:
        guard[1] = step_keys[(step_keys.index(guard[1]) + 1) % 4]
    elif mappie_np[*guard_new] == -2:
        break
    else:
        guard[0] = guard_new
print("Example 1:", len(np.where(mappie_np == 1)[1]))

# Puzzle
with open("2024/data/06_input.txt", "r") as f:
    mappie = f.readlines()
    mappie = [[l2 for l2 in l1.strip()] for l1 in mappie]

# preprocess mappie
mappie_numeric = []
for row_idx, row in enumerate(mappie):
    mappie_numeric_row = []
    for cell_idx, cell in enumerate(row):
        if cell == "#":
            mappie_numeric_row.append(-1)
        elif cell == "^":
            guard = [np.asarray([row_idx + 1, cell_idx + 1]), "N"]
            mappie_numeric_row.append(0)
        else:
            mappie_numeric_row.append(0)
    mappie_numeric.append(np.asarray(mappie_numeric_row))
mappie_np = np.pad(np.asarray(mappie_numeric), pad_width=1, constant_values=-2)

# walk the guard
while True:
    mappie_np[*guard[0]] = 1
    guard_new = guard[0] + step[guard[1]]
    if mappie_np[*guard_new] == -1:
        guard[1] = step_keys[(step_keys.index(guard[1]) + 1) % 4]
    elif mappie_np[*guard_new] == -2:
        break
    else:
        guard[0] = guard_new
print("Puzzle 1:", len(np.where(mappie_np == 1)[1]))

# for part 2
guard_passed_row, guard_passed_col = np.where(mappie_np == 1)
guard_passed = []
for row, col in zip(guard_passed_row, guard_passed_col):
    guard_passed.append(np.asarray([row, col]))


### Part 2
MAX_STEPS = 10000
# Example
with open("2024/data/06_example.txt", "r") as f:
    mappie = f.readlines()
    mappie = [[l2 for l2 in l1.strip()] for l1 in mappie]

# preprocess mappie
mappie_numeric = []
for row_idx, row in enumerate(mappie):
    mappie_numeric_row = []
    for cell_idx, cell in enumerate(row):
        if cell == "#":
            mappie_numeric_row.append(-1)
        elif cell == "^":
            guard = [np.asarray([row_idx + 1, cell_idx + 1]), "N"]
            mappie_numeric_row.append(0)
        else:
            mappie_numeric_row.append(0)
    mappie_numeric.append(np.asarray(mappie_numeric_row))
mappie_np = np.pad(np.asarray(mappie_numeric), pad_width=1, constant_values=-2)

# walk the guard
stuck = 0
for row_idx in range(1, mappie_np.shape[0] - 1):
    for col_idx in range(1, mappie_np.shape[1] - 1):
        mappie_np_paradox = mappie_np.copy()
        guard_paradox = guard.copy()

        if mappie_np_paradox[row_idx, col_idx] == -1 or (
            guard_paradox[0][0] == row_idx and guard_paradox[0][1] == col_idx
        ):
            continue
        else:
            mappie_np_paradox[row_idx, col_idx] = -1

        n = 0
        while True:
            mappie_np_paradox[*guard_paradox[0]] = 1
            guard_new = guard_paradox[0] + step[guard_paradox[1]]

            if mappie_np_paradox[*guard_new] == -1:
                guard_paradox[1] = step_keys[
                    (step_keys.index(guard_paradox[1]) + 1) % 4
                ]
            elif mappie_np_paradox[*guard_new] == -2:
                break
            elif n >= MAX_STEPS:
                stuck += 1
                break
            else:
                guard_paradox[0] = guard_new
            n += 1
print("Example 2:", stuck)


# Puzzle
with open("2024/data/06_input.txt", "r") as f:
    mappie = f.readlines()
    mappie = [[l2 for l2 in l1.strip()] for l1 in mappie]

# preprocess mappie
mappie_numeric = []
for row_idx, row in enumerate(mappie):
    mappie_numeric_row = []
    for cell_idx, cell in enumerate(row):
        if cell == "#":
            mappie_numeric_row.append(-1)
        elif cell == "^":
            guard = [np.asarray([row_idx + 1, cell_idx + 1]), "N"]
            mappie_numeric_row.append(0)
        else:
            mappie_numeric_row.append(0)
    mappie_numeric.append(np.asarray(mappie_numeric_row))
mappie_np = np.pad(np.asarray(mappie_numeric), pad_width=1, constant_values=-2)

# walk the guard
stuck = 0
for obstacle in guard_passed:
    row_idx, col_idx = obstacle
    mappie_np_paradox = mappie_np.copy()
    guard_paradox = guard.copy()

    if guard[0][0] == row_idx and guard[0][1] == col_idx:
        continue
    else:
        mappie_np_paradox[row_idx, col_idx] = -1

    n = 0
    while True:
        mappie_np_paradox[*guard_paradox[0]] = 1
        guard_new = guard_paradox[0] + step[guard_paradox[1]]

        if mappie_np_paradox[*guard_new] == -1:
            guard_paradox[1] = step_keys[(step_keys.index(guard_paradox[1]) + 1) % 4]
        elif mappie_np_paradox[*guard_new] == -2:
            break
        elif n >= MAX_STEPS:
            stuck += 1
            break
        else:
            guard_paradox[0] = guard_new
        n += 1
print("Puzzle 2:", stuck)
