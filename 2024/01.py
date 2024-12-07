# Example 1
with open("2024/data/01_example.txt", "r") as f:
    lists = f.readlines()
    lists = [l.strip() for l in lists]

l1, l2 = [], []
for item in lists:
    l1.append(int(item.split("  ")[0]))
    l2.append(int(item.split("  ")[1]))
l1 = sorted(l1)
l2 = sorted(l2)

diff = []
for item in zip(l1, l2):
    diff.append(abs(item[0] - item[1]))
print("Example 1:", sum(diff))


# Puzzle 1
with open("2024/data/01_input.txt", "r") as f:
    lists = f.readlines()
    lists = [l.strip() for l in lists]

l1, l2 = [], []
for item in lists:
    l1.append(int(item.split("  ")[0]))
    l2.append(int(item.split("  ")[1]))
l1 = sorted(l1)
l2 = sorted(l2)

diff = []
for item in zip(l1, l2):
    diff.append(abs(item[0] - item[1]))
print("Puzzle 1:", sum(diff))


# Example 2
with open("2024/data/01_example.txt", "r") as f:
    lists = f.readlines()
    lists = [l.strip() for l in lists]

l1, l2 = [], []
for item in lists:
    l1.append(int(item.split("  ")[0]))
    l2.append(int(item.split("  ")[1]))
l1 = sorted(l1)
l2 = sorted(l2)

l1_mult = []
for item in l1:
    l1_mult.append(item * l2.count(item))
print("Example 2:", sum(l1_mult))


# Puzzle 2
with open("2024/data/01_input.txt", "r") as f:
    example = f.readlines()
    example = [l.strip() for l in example]

l1, l2 = [], []
for item in example:
    l1.append(int(item.split("  ")[0]))
    l2.append(int(item.split("  ")[1]))
l1 = sorted(l1)
l2 = sorted(l2)

l1_mult = []
for item in l1:
    l1_mult.append(item * l2.count(item))
print("Puzzle 2:", sum(l1_mult))
