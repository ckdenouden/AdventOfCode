from collections import defaultdict


### Part 1
def get_regions(patch: tuple, start: bool = False) -> list[tuple]:
    row, col = patch
    if start:
        REGIONS[GARDEN[row][col]] += [[patch]]
    else:
        REGIONS[GARDEN[row][col]][-1].append(patch)
    del PATCHES[GARDEN[row][col]][PATCHES[GARDEN[row][col]].index(patch)]

    neighbours = [
        n
        for n in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        if 0 <= n[0] < len(GARDEN)
        and 0 <= n[1] < len(GARDEN[0])
        and GARDEN[n[0]][n[1]] == GARDEN[row][col]
    ]
    if neighbours:
        for neighbour in neighbours:
            if neighbour not in sum(REGIONS[GARDEN[row][col]], []):
                get_regions(neighbour)


def get_neighbours(patch: tuple) -> list:
    return [
        GARDEN[n[0]][n[1]]
        for n in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        if 0 <= n[0] < len(GARDEN)
        and 0 <= n[1] < len(GARDEN[0])
        and GARDEN[patch[0]][patch[1]] != GARDEN[n[0]][n[1]]
    ]


# Example
# with open("2024/data/12_example.txt", "r") as f:
#     GARDEN = f.readlines()
#     GARDEN = [[l2 for l2 in l1.strip()] for l1 in GARDEN]

# PATCHES = defaultdict(list)
# for row in range(len(GARDEN)):
#     for col in range(len(GARDEN[row])):
#         PATCHES[GARDEN[row][col]].append((row, col))

# REGIONS = defaultdict(list)
# while len(sum(PATCHES.values(), [])):
#     for plant in sorted(list(set(sum(GARDEN, [])))):
#         if PATCHES[plant]:
#             get_regions(PATCHES[plant][0], start=True)

# PERIMETER = defaultdict(list)
# for region_plant, region_patches in REGIONS.items():
#     for region_patch in region_patches:
#         PERIMETER[region_plant] += [[0, 0]]
#         for patch in region_patch:
#             row, col = patch
#             if row == 0 or row == len(GARDEN) - 1:
#                 PERIMETER[region_plant][-1][0] += 1
#             if col == 0 or col == len(GARDEN[row]) - 1:
#                 PERIMETER[region_plant][-1][0] += 1
#             PERIMETER[region_plant][-1][1] += len(get_neighbours(patch))

# # calculate cost
# cost = 0
# for plant, perimeters in PERIMETER.items():
#     regions = REGIONS[plant]
#     for region, perimeter in zip(regions, perimeters):
#         cost += len(region) * (perimeter[0] + perimeter[1])
# print("Example 1:", cost)


# # Puzzle
# with open("2024/data/12_input.txt", "r") as f:
#     GARDEN = f.readlines()
#     GARDEN = [[l2 for l2 in l1.strip()] for l1 in GARDEN]

# PATCHES = defaultdict(list)
# for row in range(len(GARDEN)):
#     for col in range(len(GARDEN[row])):
#         PATCHES[GARDEN[row][col]].append((row, col))

# REGIONS = defaultdict(list)
# while len(sum(PATCHES.values(), [])):
#     for plant in sorted(list(set(sum(GARDEN, [])))):
#         if PATCHES[plant]:
#             get_regions(PATCHES[plant][0], start=True)

# PERIMETER = defaultdict(list)
# for region_plant, region_patches in REGIONS.items():
#     for region_patch in region_patches:
#         PERIMETER[region_plant] += [[0, 0]]
#         for patch in region_patch:
#             row, col = patch
#             if row == 0 or row == len(GARDEN) - 1:
#                 PERIMETER[region_plant][-1][0] += 1
#             if col == 0 or col == len(GARDEN[row]) - 1:
#                 PERIMETER[region_plant][-1][0] += 1
#             PERIMETER[region_plant][-1][1] += len(get_neighbours(patch))

# # calculate cost
# cost = 0
# for plant, perimeters in PERIMETER.items():
#     regions = REGIONS[plant]
#     for region, perimeter in zip(regions, perimeters):
#         cost += len(region) * (perimeter[0] + perimeter[1])
# print("Puzzle 1:", cost)


### Part 2
def get_sides(region):
    print(region)

    sides = 0

    for row in range(len(GARDEN)):
        INNER = False
        for col in range(len(GARDEN[0])):
            if (row, col) in region and not INNER:
                INNER = True
                sides += 1
            elif (row, col) not in region and INNER:
                INNER = False
    for row in reversed(range(len(GARDEN))):
        INNER = False
        for col in range(len(GARDEN[0])):
            if (row, col) in region and not INNER:
                INNER = True
                sides += 1
            elif (row, col) not in region and INNER:
                INNER = False

    print(sides)


# Example
with open("2024/data/12_example.txt", "r") as f:
    GARDEN = f.readlines()
    GARDEN = [[l2 for l2 in l1.strip()] for l1 in GARDEN]

PATCHES = defaultdict(list)
for row in range(len(GARDEN)):
    for col in range(len(GARDEN[row])):
        PATCHES[GARDEN[row][col]].append((row, col))

REGIONS = defaultdict(list)
while len(sum(PATCHES.values(), [])):
    for plant in sorted(list(set(sum(GARDEN, [])))):
        if PATCHES[plant]:
            get_regions(PATCHES[plant][0], start=True)

SIDES = defaultdict(list)
for region_plant, regions in REGIONS.items():
    for region in regions:
        get_sides(region)
        break
    break


# PERIMETER = defaultdict(list)
# for region_plant, region_patches in REGIONS.items():
#     for region_patch in region_patches:
#         PERIMETER[region_plant] += [[0, 0]]
#         for patch in region_patch:
#             row, col = patch
#             if row == 0 or row == len(GARDEN) - 1:
#                 PERIMETER[region_plant][-1][0] += 1
#             if col == 0 or col == len(GARDEN[row]) - 1:
#                 PERIMETER[region_plant][-1][0] += 1
#             PERIMETER[region_plant][-1][1] += len(get_neighbours(patch))


# # calculate cost
# cost = 0
# for plant, perimeters in PERIMETER.items():
#     regions = REGIONS[plant]
#     for region, perimeter in zip(regions, perimeters):
#         cost += len(region) * (perimeter[0] + perimeter[1])
# print("Example 1:", cost)


# Puzzle
