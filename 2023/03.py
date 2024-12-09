import re
import string
from collections import defaultdict

symbols = "".join(set(string.punctuation) - set("."))

engine = []
with open("03a.txt", "r") as f:
    for line in f.readlines():
        engine += [line.strip("\n")]

parts = []
for idx, layer in enumerate(engine):
    matches = re.finditer(r"\d+", layer)
    for match in matches:
        start, end = match.start(), match.end() - 1

        if idx in range(1, len(engine)) and re.search(
            rf"[{re.escape(symbols)}]", engine[idx - 1][max(0, start - 1) : min(end + 2, len(engine[0]) - 1)]
        ):
            parts.append(int(match.group(0)))
        elif idx in range(len(engine) - 2) and re.search(
            rf"[{re.escape(symbols)}]", engine[idx + 1][max(0, start - 1) : min(end + 2, len(engine[0]) - 1)]
        ):
            parts.append(int(match.group(0)))
        elif (start > 0 and engine[idx][start - 1] in symbols) or (
            end < len(engine[0]) - 2 and engine[idx][end + 1] in symbols
        ):
            parts.append(int(match.group(0)))
print(sum(parts))


gears = []
for idx, layer in enumerate(engine):
    matches = re.finditer(r"[*]", layer)
    for m in matches:
        gears += [(idx, m.start())]

gear_adjacents = defaultdict(lambda: [])
for gear in gears:
    print(gear)
    gear_r, gear_c = gear

    adjacents = [
        (gear_r, gear_c + 1),
        (gear_r, gear_c - 1),
        (gear_r + 1, gear_c + 1),
        (gear_r + 1, gear_c - 1),
        (gear_r - 1, gear_c + 1),
        (gear_r - 1, gear_c - 1),
        (gear_r + 1, gear_c),
        (gear_r - 1, gear_c),
    ]
    for adjacent in adjacents:
        if adjacent[0] in range(len(engine)) and adjacent[1] in range(len(engine[0])):
            gear_adjacents.append(adjacent)
    gear_adjacents = sorted(gear_adjacents)
    print(gear_adjacents)
    break


for idx, layer in enumerate(engine):
    matches = re.finditer(r"\d+", layer)
    for match in matches:
        print(match)
        match_coordinates = [(idx, col) for col in range(match.start(), match.end())]
        print(match_coordinates)
#         start, end = m.start(), m.end() - 1

#         if idx in range(1, len(engine)):
#             if gear := re.search(r"[*]", engine[idx - 1]):
#                 print(gear)
#                 gears[f"{idx-1},{gear.start()}"] += [m.group(0)]
#         elif idx in range(len(engine) - 2):
#             if gear := re.search(r"[*]", engine[idx + 1]):
#                 print(gear)
#                 gears[f"{idx+1},{gear.start()}"] += [m.group(0)]
#         elif start > 0 and engine[idx][start - 1] == "*":
#             gears[f"({idx},{start - 1})"] += [m.group(0)]
#         elif end < len(engine[0]) - 2 and engine[idx][end + 1] == "*":
#             gears[f"({idx},{end + 1})"] += [m.group(0)]
# 467835

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
