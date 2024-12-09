walls = set()
blizzards = set()
for idx_y, line in enumerate(open("day24.txt")):
    for idx_x, c in enumerate(line):
        if c == ">":
            blizzards.add(((idx_x-1, idx_y-1), (1, 0)))
        elif c == "v":
            blizzards.add(((idx_x-1, idx_y-1), (0, 1)))
        elif c == "<":
            blizzards.add(((idx_x-1, idx_y-1), (-1, 0)))
        elif c == "^":
            blizzards.add(((idx_x-1, idx_y-1), (0, -1)))
        if c == "#":
            walls.add((idx_x-1, idx_y-1))
walls.add((0, -2))
walls.add((100, 35))
x_max = max(x for x, _ in walls)
y_max = max(y for _, y in walls)


start = (0, -1)
positions = set()
positions.add(start)
target = (99, 35)

t = 0
while True:
    t += 1
    
    blizzards_next = {((pos[0] + change[0]*t) % x_max, (pos[1] + change[1]*t) % y_max) for pos, change in blizzards}
    positions_next = {(pos[0] + change[0], pos[1] + change[1]) for change in [(0,0), (1,0), (0,1), (-1,0), (0,-1)] for pos in positions}
    positions = positions_next - walls - blizzards_next

    if target in positions:
        print("Target reached after", t, "minutes")
        break


start = (0, -1)
positions = set()
positions.add(start)
target = (99, 35)
targets = [target, start, target]

t = 0
while True:
    t += 1
    if len(targets) == 0:
        break
    
    blizzards_next = {((pos[0] + change[0]*t) % x_max, (pos[1] + change[1]*t) % y_max) for pos, change in blizzards}
    positions_next = {(pos[0] + change[0], pos[1] + change[1]) for change in [(0,0), (1,0), (0,1), (-1,0), (0,-1)] for pos in positions}
    positions = positions_next - walls - blizzards_next

    if targets[0] in positions:
        print("Target reached after", t, "minutes")
        positions = set()
        positions.add(targets.pop(0))