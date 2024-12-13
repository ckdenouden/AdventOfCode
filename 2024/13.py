from collections import defaultdict


### Part 1
COST = {"A": 3, "B": 1}
# Example
with open("2024/data/13_example.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

MACHINES = []
machine = dict()
for line in CONFIGURATION:
    if line.startswith("Button A"):
        machine["A"] = tuple([int(n[1:].strip("+,")) for n in line.split(" ")[2:]])
    elif line.startswith("Button B"):
        machine["B"] = tuple([int(n[1:].strip("+,")) for n in line.split(" ")[2:]])
    elif line.startswith("Prize"):
        machine["P"] = tuple([int(n[2:].strip(",")) for n in line.split(" ")[1:]])
        MACHINES.append(machine)
        machine = dict()

TOTAL_COST = 0
for machine in MACHINES:
    c2 = (machine["A"][0] * machine["P"][1] - machine["A"][1] * machine["P"][0]) / (
        machine["A"][0] * machine["B"][1] - machine["A"][1] * machine["B"][0]
    )
    c1 = (machine["P"][0] - c2 * machine["B"][0]) / machine["A"][0]
    if c1.is_integer() and c2.is_integer():
        TOTAL_COST += COST["A"] * int(c1) + COST["B"] * int(c2)
print("Example 1:", TOTAL_COST)

# Puzzle
with open("2024/data/13_input.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

MACHINES = []
machine = dict()
for line in CONFIGURATION:
    if line.startswith("Button A"):
        machine["A"] = tuple([int(n[1:].strip("+,")) for n in line.split(" ")[2:]])
    elif line.startswith("Button B"):
        machine["B"] = tuple([int(n[1:].strip("+,")) for n in line.split(" ")[2:]])
    elif line.startswith("Prize"):
        machine["P"] = tuple([int(n[2:].strip(",")) for n in line.split(" ")[1:]])
        MACHINES.append(machine)
        machine = dict()

TOTAL_COST = 0
for machine in MACHINES:
    c2 = (machine["A"][0] * machine["P"][1] - machine["A"][1] * machine["P"][0]) / (
        machine["A"][0] * machine["B"][1] - machine["A"][1] * machine["B"][0]
    )
    c1 = (machine["P"][0] - c2 * machine["B"][0]) / machine["A"][0]
    if c1.is_integer() and c2.is_integer():
        TOTAL_COST += COST["A"] * int(c1) + COST["B"] * int(c2)
print("Puzzle 1:", TOTAL_COST)

### Part 2
# Example
with open("2024/data/13_example.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

MACHINES = []
machine = dict()
for line in CONFIGURATION:
    if line.startswith("Button A"):
        machine["A"] = tuple([int(n[1:].strip("+,")) for n in line.split(" ")[2:]])
    elif line.startswith("Button B"):
        machine["B"] = tuple([int(n[1:].strip("+,")) for n in line.split(" ")[2:]])
    elif line.startswith("Prize"):
        machine["P"] = tuple([int(n[2:].strip(",")) + 10000000000000 for n in line.split(" ")[1:]])
        MACHINES.append(machine)
        machine = dict()

TOTAL_COST = 0
for machine in MACHINES:
    c2 = (machine["A"][0] * machine["P"][1] - machine["A"][1] * machine["P"][0]) / (
        machine["A"][0] * machine["B"][1] - machine["A"][1] * machine["B"][0]
    )
    c1 = (machine["P"][0] - c2 * machine["B"][0]) / machine["A"][0]
    if c1.is_integer() and c2.is_integer():
        TOTAL_COST += COST["A"] * int(c1) + COST["B"] * int(c2)
print("Example 2:", TOTAL_COST)

# Puzzle
with open("2024/data/13_input.txt", "r") as f:
    CONFIGURATION = f.readlines()
    CONFIGURATION = [l.strip() for l in CONFIGURATION]

MACHINES = []
machine = dict()
for line in CONFIGURATION:
    if line.startswith("Button A"):
        machine["A"] = tuple([int(n[1:].strip("+,")) for n in line.split(" ")[2:]])
    elif line.startswith("Button B"):
        machine["B"] = tuple([int(n[1:].strip("+,")) for n in line.split(" ")[2:]])
    elif line.startswith("Prize"):
        machine["P"] = tuple([int(n[2:].strip(",")) + 10000000000000 for n in line.split(" ")[1:]])
        MACHINES.append(machine)
        machine = dict()

TOTAL_COST = 0
for machine in MACHINES:
    c2 = (machine["A"][0] * machine["P"][1] - machine["A"][1] * machine["P"][0]) / (
        machine["A"][0] * machine["B"][1] - machine["A"][1] * machine["B"][0]
    )
    c1 = (machine["P"][0] - c2 * machine["B"][0]) / machine["A"][0]
    if c1.is_integer() and c2.is_integer():
        TOTAL_COST += COST["A"] * int(c1) + COST["B"] * int(c2)
print("Puzzle 2:", TOTAL_COST)
