import re

crates = [
    ["Q", "W", "P", "S", "Z", "R", "H", "D"],
    ["V", "B", "R", "W", "Q", "H", "F"],
    ["C", "V", "S", "H"],
    ["H", "F", "G"],
    ["P", "G", "J", "B", "Z"],
    ["Q", "T", "J", "H", "W", "F", "L"],
    ["Z", "T", "W", "D", "L", "V", "J", "N"],
    ["D", "T", "Z", "C", "J", "G", "H", "F"],
    ["W", "P", "V", "M", "B", "H"]
]
with open("day05.txt", "r") as f:
    for line in f.readlines()[10:]:
        extracted = re.findall(r'\d+', line)
        steps = int(extracted[0])
        stack_from = int(extracted[1])-1
        stack_to = int(extracted[2])-1
        # for step in range(steps):                                 # Part 1
        #     crates[stack_to].append(crates[stack_from].pop())     # Part 1
        crates[stack_to] += crates[stack_from][-steps:]             # Part 2
        del crates[stack_from][-steps:]                             # Part 2
[print(c[-1]) for c in crates]