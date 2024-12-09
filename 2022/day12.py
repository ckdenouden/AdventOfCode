import numpy as np

position = (20, 0)
visited = [position]
def get_best(pos):
    adjacent = [
        (pos[0], pos[1]+1),
        (pos[0]+1, pos[1]),
        (pos[0], pos[1]-1),
        (pos[0]-1, pos[1])
    ]

    options = []
    for i in range(len(adjacent)):
        if 0 <= adjacent[i][0] < heightmap.shape[0]:
            if 0 <= adjacent[i][1] < heightmap.shape[1]:
                if heightmap[adjacent[i]] - heightmap[pos] <= 1:
                    if adjacent[i] not in visited:
                        options.append(i)
    
    if options == []:
        return 0

    options_dist = [np.linalg.norm(adjacent[o]-peak) for o in options]
    best = adjacent[options[options_dist.index(np.min(options_dist))]]
    visited.append(pos)
    return best


#heightmap = np.zeros((5, 8), dtype=int)
heightmap = np.zeros((41, 113), dtype=int)
with open("day12.txt", "r") as f:
    for idx_y, line in enumerate(f.readlines()):
        line = list(line.strip())
        for idx_x, char in enumerate(line):
            heightmap[idx_y, idx_x] = ord(char)-96
            if char == "E":
                heightmap[idx_y, idx_x] = 27
                peak = np.array((idx_y, idx_x))
            elif char == "S":
                heightmap[idx_y, idx_x] = 1
    #print(heightmap)





steps = 0
backtrack = 1
while True:
    position = get_best(position)
    if position == 0:
        backtrack += 1
        position = visited[-backtrack]
        print(position, backtrack)
        continue
    else:
        steps += 1
        backtrack = 1
    print(position)
    visited.append(position)

    if heightmap[position] == 27:
        break
    
print("Steps:", steps)