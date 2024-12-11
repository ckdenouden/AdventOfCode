from collections import defaultdict
from functools import cache


@cache
def blink(stone: str) -> list:
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        return [
            stone[: len(stone) // 2],
            stone_stripped if (stone_stripped := stone[len(stone) // 2 :].lstrip("0")) else "0",
        ]
    else:
        return [str(int(stone) * 2024)]


### Part 1
BLINKS = 25
# Example
with open("2024/data/11_example.txt", "r") as f:
    stones_init = f.readlines()
    stones_init = sum([l.strip().split() for l in stones_init], [])

stones = stones_init.copy()
for _ in range(BLINKS):
    stones_new = []
    for stone in stones:
        stones_new += blink(stone)
    stones = stones_new.copy()
print("Example 1:", len(stones))

# Puzzle
with open("2024/data/11_input.txt", "r") as f:
    stones_init = f.readlines()
    stones_init = sum([l.strip().split() for l in stones_init], [])

stones = stones_init.copy()
for _ in range(BLINKS):
    stones_new = []
    for stone in stones:
        stones_new += blink(stone)
    stones = stones_new.copy()
print("Puzzle 1:", len(stones))


### Part 2
BLINKS = 75
# Example
with open("2024/data/11_example.txt", "r") as f:
    stones_init = f.readlines()
    stones_init = sum([l.strip().split() for l in stones_init], [])

stones = defaultdict(int)
for stone in stones_init:
    stones[stone] += 1

for _ in range(BLINKS):
    for stone, n in stones.copy().items():
        stones[stone] -= n
        for stone_new in blink(stone):
            stones[stone_new] += n
    for stone in [k for k, v in stones.items() if v == 0]:
        del stones[stone]
print("Example 2:", sum(stones.values()))

# Puzzle
with open("2024/data/11_input.txt", "r") as f:
    stones_init = f.readlines()
    stones_init = sum([l.strip().split() for l in stones_init], [])

stones = defaultdict(int)
for stone in stones_init:
    stones[stone] += 1

for _ in range(BLINKS):
    for stone, n in stones.copy().items():
        stones[stone] -= n
        for stone_new in blink(stone):
            stones[stone_new] += n
    for stone in [k for k, v in stones.items() if v == 0]:
        del stones[stone]
print("Puzzle 2:", sum(stones.values()))
