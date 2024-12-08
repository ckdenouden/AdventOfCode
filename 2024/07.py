import re


def get_equations(values: list) -> list:
    if None not in values:
        return values
    else:
        values_local = values.copy()

    equations = [values_local]
    for idx, val in enumerate(values_local):
        if idx == len(values_local) - 1:
            return equations
        elif val == None:
            for op in OPERATIONS.keys():
                values_local[idx] = op
                equations.append(values_local.copy())
            equations.pop(-len(OPERATIONS) - 1)
            break

    to_pop = []
    for idx_eq, equation in enumerate(equations):
        if None in equation and idx_eq not in to_pop:
            to_pop.append(idx_eq)
            equations += get_equations(equation)

    for idx_pop in sorted(to_pop, reverse=True):
        del equations[idx_pop]
    return equations


def eval_equation(equation: list) -> int:
    eval_a, eval_op, eval_b = equation[:3]
    equation = equation[3:]
    agg_value = OPERATIONS[eval_op](eval_a, eval_b)
    while equation:
        eval_op, eval_b = equation[:2]
        agg_value = OPERATIONS[eval_op](agg_value, eval_b)
        equation = equation[2:]
    return agg_value


### Part 1
OPERATIONS = {
    "*": lambda a, b: int(a) * int(b),
    "+": lambda a, b: int(a) + int(b),
}
# Example
with open("2024/data/07_example.txt", "r") as f:
    calibrations = f.readlines()
    calibrations = [l.strip() for l in calibrations]
    calibrations = [re.split(r"(?:: )|(?: )", l) for l in calibrations]

calibration_results = []
for calibration in calibrations:
    answer = int(calibration[0])
    values = calibration[1:]

    values_with_operators = values.copy()
    i = 1
    while len(values_with_operators) < 2 * len(values) - 1:
        values_with_operators.insert(i, None)
        i += 2

    equations = get_equations(values_with_operators)

    correct = False
    for equation in equations:
        if eval_equation(equation) == answer:
            calibration_results.append(answer)
            break

print("Example 1:", sum(calibration_results))


# Puzzle
with open("2024/data/07_input.txt", "r") as f:
    calibrations = f.readlines()
    calibrations = [l.strip() for l in calibrations]
    calibrations = [re.split(r"(?:: )|(?: )", l) for l in calibrations]

calibration_results = []
for c, calibration in enumerate(calibrations):
    print(f"{c}/{len(calibrations)}: {calibration}")
    answer = int(calibration[0])
    values = calibration[1:]

    values_with_operators = values.copy()
    i = 1
    while len(values_with_operators) < 2 * len(values) - 1:
        values_with_operators.insert(i, None)
        i += 2

    equations = get_equations(values_with_operators)

    correct = False
    for equation in equations:
        if eval_equation(equation) == answer:
            calibration_results.append(answer)
            break
print("Puzzle 1:", sum(calibration_results))

### Part 2
OPERATIONS = {
    "*": lambda a, b: int(a) * int(b),
    "+": lambda a, b: int(a) + int(b),
    "||": lambda a, b: int(str(a) + str(b)),
}
# Example
with open("2024/data/07_example.txt", "r") as f:
    calibrations = f.readlines()
    calibrations = [l.strip() for l in calibrations]
    calibrations = [re.split(r"(?:: )|(?: )", l) for l in calibrations]

calibration_results = []
for calibration in calibrations:
    answer = int(calibration[0])
    values = calibration[1:]

    values_with_operators = values.copy()
    i = 1
    while len(values_with_operators) < 2 * len(values) - 1:
        values_with_operators.insert(i, None)
        i += 2

    equations = get_equations(values_with_operators)

    correct = False
    for equation in equations:
        if eval_equation(equation) == answer:
            calibration_results.append(answer)
            break
print("Example 2:", sum(calibration_results))

# Puzzle
with open("2024/data/07_input.txt", "r") as f:
    calibrations = f.readlines()
    calibrations = [l.strip() for l in calibrations]
    calibrations = [re.split(r"(?:: )|(?: )", l) for l in calibrations]

calibration_results = []
for c, calibration in enumerate(calibrations):
    print(f"{c}/{len(calibrations)}: {calibration}")
    answer = int(calibration[0])
    values = calibration[1:]

    values_with_operators = values.copy()
    i = 1
    while len(values_with_operators) < 2 * len(values) - 1:
        values_with_operators.insert(i, None)
        i += 2

    equations = get_equations(values_with_operators)

    correct = False
    for equation in equations:
        if eval_equation(equation) == answer:
            calibration_results.append(answer)
            break
print("Puzzle 2:", sum(calibration_results))
