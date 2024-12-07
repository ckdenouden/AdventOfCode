XMAS = "XMAS"

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def is_xmas(puzzle: list, row: int, col: int, agg: str = "", d_idx: int = -1):
    agg += puzzle[row][col]

    if not XMAS.startswith(agg) or len(agg) > 4:
        return False
    elif XMAS == agg:
        return True
    else:
        xmasses = 0
        if d_idx == -1:
            for idx, direction in enumerate(directions):
                if (
                    row + direction[0] >= 0
                    and row + direction[0] <= len(puzzle) - 1
                    and col + direction[1] >= 0
                    and col + direction[1] <= len(puzzle[0]) - 1
                ):
                    xmasses += is_xmas(
                        puzzle, row + direction[0], col + direction[1], agg, idx
                    )
        else:
            if (
                row + directions[d_idx][0] >= 0
                and row + directions[d_idx][0] <= len(puzzle) - 1
                and col + directions[d_idx][1] >= 0
                and col + directions[d_idx][1] <= len(puzzle[0]) - 1
            ):
                xmasses += is_xmas(
                    puzzle,
                    row + directions[d_idx][0],
                    col + directions[d_idx][1],
                    agg,
                    d_idx,
                )
        return xmasses


def is_mas(puzzle: list, row: int, col: int, mass: list):
    if (
        puzzle[row][col] == mass[0][0]
        and puzzle[row][col + 2] == mass[0][1]
        and puzzle[row + 1][col + 1] == "A"
        and puzzle[row + 2][col] == mass[1][0]
        and puzzle[row + 2][col + 2] == mass[1][1]
    ):
        return 1
    return 0


### Part 1
# Example
with open("2024/data/04_example.txt", "r") as f:
    puzzle = f.readlines()
    puzzle = [[l2 for l2 in l1.strip()] for l1 in puzzle]

row, col = 0, 0
xmasses = 0
for _ in range(len(puzzle[0]) ** 2):
    if puzzle[row][col] == "X":
        xmasses += is_xmas(puzzle, row, col)

    # move to next spot
    col += 1
    col %= len(puzzle[0])
    if col == 0:
        row += 1
print("Example 1:", xmasses)

# Puzzle
with open("2024/data/04_input.txt", "r") as f:
    puzzle = f.readlines()
    puzzle = [[l2 for l2 in l1.strip()] for l1 in puzzle]

row, col = 0, 0
xmasses = 0
for _ in range(len(puzzle[0]) ** 2):
    if puzzle[row][col] == "X":
        xmasses += is_xmas(puzzle, row, col)

    # move to next spot
    col += 1
    col %= len(puzzle[0])
    if col == 0:
        row += 1
print("Puzzle 1:", xmasses)

### Part 2 - convolution approach
MASSES = [
    [["M", "S"], ["M", "S"]],
    [["M", "M"], ["S", "S"]],
    [["S", "M"], ["S", "M"]],
    [["S", "S"], ["M", "M"]],
]
# Example
with open("2024/data/04_example.txt", "r") as f:
    puzzle = f.readlines()
    puzzle = [[l2 for l2 in l1.strip()] for l1 in puzzle]

row, col = 0, 0
xmasses = 0
for _ in range((len(puzzle[0]) - 2) ** 2):
    for mass in MASSES:
        xmasses += is_mas(puzzle, row, col, mass)

    # move to next spot
    col += 1
    col %= len(puzzle[0]) - 2
    if col == 0:
        row += 1
print("Example 2:", xmasses)


# Puzzle
with open("2024/data/04_input.txt", "r") as f:
    puzzle = f.readlines()
    puzzle = [[l2 for l2 in l1.strip()] for l1 in puzzle]

row, col = 0, 0
xmasses = 0
for _ in range((len(puzzle[0]) - 2) ** 2):
    for mass in MASSES:
        xmasses += is_mas(puzzle, row, col, mass)

    # move to next spot
    col += 1
    col %= len(puzzle[0]) - 2
    if col == 0:
        row += 1
print("Puzzle 2:", xmasses)
