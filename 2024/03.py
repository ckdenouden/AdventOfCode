import re


### Part 1
pattern_1 = re.compile(r"mul\(([\d]+),([\d]+)\)")
# Example
with open("2024/data/03_example_1.txt", "r") as f:
    memory = f.readlines()
    memory = "".join([l.strip() for l in memory])

sum = 0
for match in re.findall(pattern_1, memory):
    sum += int(match[0]) * int(match[1])
print("Example 1:", sum)


# Puzzle
with open("2024/data/03_input.txt", "r") as f:
    memory = f.readlines()
    memory = "".join([l.strip() for l in memory])

sum = 0
for match in re.findall(pattern_1, memory):
    sum += int(match[0]) * int(match[1])
print("Puzzle 1:", sum)


### Part 2
pattern_2 = re.compile(r"(mul\(([\d]+),([\d]+)\))|(don't\(\))|(do\(\))")
# Example
with open("2024/data/03_example_2.txt", "r") as f:
    memory = f.readlines()
    memory = "".join([l.strip() for l in memory])

sum = 0
active = True
for match in re.finditer(pattern_2, memory):
    if match.group() == "don't()":
        active = False
    elif match.group() == "do()":
        active = True
    elif active:
        sum += int(match.group(2)) * int(match.group(3))
print("Example 2:", sum)


# Puzzle
with open("2024/data/03_input.txt", "r") as f:
    memory = f.readlines()
    memory = "".join([l.strip() for l in memory])

sum = 0
active = True
for match in re.finditer(pattern_2, memory):
    if match.group() == "don't()":
        active = False
    elif match.group() == "do()":
        active = True
    elif active:
        sum += int(match.group(2)) * int(match.group(3))
print("Puzzle 2:", sum)
