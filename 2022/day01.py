elves, calories = [], 0
with open("day01.txt", "r") as f:
    for line in f.readlines():
        if line == "\n":
            elves.append(calories)
            calories = 0
            continue
        calories += int(line.replace("\n", ""))
print("Max calories:", max(elves))
print("Top 3 sum:", sum(sorted(elves)[-3:]))