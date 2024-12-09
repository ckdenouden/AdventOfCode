import matplotlib.pyplot as plt
import numpy as np


map_list = []
max_len = 150
with open("day22.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()
        if len(line) == 0:
            continue
        if len(line) > 0 and line[0] not in [" ", ".", "#"]:
            instruction_string = line
            break
        line = line.replace(" ", "-1,")
        line = line.replace(".", "0,")
        line = line.replace("#", "1,")
        line_map = [int(l) for l in line.split(",") if len(l) > 0]
        if len(line_map) < max_len:
            line_map += [-1] * (max_len-len(line_map))
        map_list.append(line_map)
    map_arr = np.pad(np.asarray(map_list), 1, constant_values=-1)

    instructions = []
    while len(instruction_string) > 0:
        instruction_L_part = instruction_string.partition("L")
        instruction_L = instruction_L_part[:2]
        instruction_string_L = instruction_L_part[2]
        instruction_R_part = instruction_string.partition("R")
        instruction_R = instruction_R_part[:2]
        instruction_string_R = instruction_R_part[2]
        if len("".join(instruction_L_part[:2])) <= 3:
            instructions += instruction_L
            instruction_string = instruction_string_L
        elif len("".join(instruction_R_part[:2])) <= 3:
            instructions += instruction_R
            instruction_string = instruction_string_R
    instructions.pop()


wrappings = dict()
for i in range(50):
    wrappings.update({((100, 1+i), "U"): ((51+i, 51), "R")})
    wrappings.update({((51+i, 50), "L"): ((1+i, 101), "D")})
    wrappings.update({((1+i, 50), "L"): ((150-i, 1), "R")})
    wrappings.update({((0, 51+i), "U"): ((151+i, 1), "R")})
    wrappings.update({((0, 101+i), "U"): ((200, 1+i), "U")})
    wrappings.update({((1+i, 151), "R"): ((150-i, 100), "L")})
    wrappings.update({((51, 101+i), "D"): ((51+i, 101), "L")})
    wrappings.update({((51+i, 101), "R"): ((50, 101+i), "U")})
    wrappings.update({((101+i, 101), "R"): ((50-i, 151), "L")})
    wrappings.update({((151, 51+i), "D"): ((151+i, 50), "L")})
    wrappings.update({((151+i, 51), "R"): ((150, 51+i), "U")})
    wrappings.update({((201, 1+i), "D"): ((1, 101+i), "D")})
    wrappings.update({((151+i, 0), "L"): ((1, 51+i), "D")})
    wrappings.update({((101+i, 0), "L"): ((50-i, 51), "R")})


plt.imshow(map_arr)
plt.show()

facings = ["R", "D", "L", "U"]
facing = "R"
position = (1, 51)
map_arr[position] = 2
for instr in instructions:
    if instr.isalpha():
        if instr == "R":
            facing = facings[(facings.index(facing)+1)%4]
        elif instr == "L":
            facing = facings[(facings.index(facing)-1)%4]
        continue
        
    steps = int(instr)
    for i in range(steps):
        if facing == "R":
            position_new = (position[0], position[1]+1)
            if map_arr[position_new] in [0, 2]:
                position = position_new
                map_arr[position] = 2
            elif map_arr[position_new] == 1:
                break
            elif map_arr[position_new] == -1:
                wrapped, facing_new = wrappings[(position_new, facing)] #(position[0], next((i for i, x in enumerate(map_arr[position[0], :]) if x >= 0), None))

                if map_arr[wrapped] in [0, 2]:
                    position = wrapped
                    facing = facing_new
                    map_arr[wrapped] = 2
                elif map_arr[wrapped] == 1:
                    break
        elif facing == "D":
            position_new = (position[0]+1, position[1])
            if map_arr[position_new] in [0, 2]:
                position = position_new
                map_arr[position] = 2
            elif map_arr[position_new] == 1:
                break
            elif map_arr[position_new] == -1:
                wrapped, facing_new = wrappings[(position_new, facing)] #(next((i for i, x in enumerate(map_arr[:, position[1]]) if x >= 0), None), position[1])
                if map_arr[wrapped] in [0, 2]:
                    position = wrapped
                    facing = facing_new
                    map_arr[wrapped] = 2
                elif map_arr[wrapped] == 1:
                    break
        elif facing == "L":
            position_new = (position[0], position[1]-1)
            if map_arr[position_new] in [0, 2]:
                position = position_new
                map_arr[position] = 2
            elif map_arr[position_new] == 1:
                break
            elif map_arr[position_new] == -1:
                wrapped, facing_new = wrappings[(position_new, facing)] #(position[0], next((i for i, x in reversed(list(enumerate(map_arr[position[0], :]))) if x >= 0), None))
                if map_arr[wrapped] in [0, 2]:
                    position = wrapped
                    facing = facing_new
                    map_arr[wrapped] = 2
                elif map_arr[wrapped] == 1:
                    break
        elif facing == "U":
            position_new = (position[0]-1, position[1])
            if map_arr[position_new] in [0, 2]:
                position = position_new
                map_arr[position] = 2
            elif map_arr[position_new] == 1:
                break
            elif map_arr[position_new] == -1:
                wrapped, facing_new = wrappings[(position_new, facing)] #(next((i for i, x in reversed(list(enumerate(map_arr[:, position[1]]))) if x >= 0), None), position[1])
                if map_arr[wrapped] in [0, 2]:
                    position = wrapped
                    facing = facing_new
                    map_arr[wrapped] = 2
                elif map_arr[wrapped] == 1:
                    break

plt.imshow(map_arr)
plt.show()

print(position[0], position[1], facings.index(facing))
print(sum((1000*position[0], 4*position[1], facings.index(facing))))