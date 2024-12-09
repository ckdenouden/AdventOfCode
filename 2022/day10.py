cycle, register = 0, 1
add, prev_add = 0, 0
signal_strength = 0

screen = []
with open("day10.txt", "r") as f:
    for idx, line in enumerate(f.readlines()):
        cycle += 1
        line = line.strip()

        register_block = [register, register+1, register+2]
        if cycle % 40 in register_block:

            screen.append("#")
        else:
            screen.append(".")
        
        if cycle % 40 == 0:
            print(screen)
            screen = []

        if cycle % 40 == 20:
            #print(idx, cycle, register, (line, prev_add))
            signal_strength += cycle*register
        
        if line.split(" ")[0] == "addx":
            cycle += 1

            register_block = [register, register+1, register+2]
            if cycle % 40 in register_block:
                screen.append("#")
            else:
                screen.append(".")
            
            if cycle % 40 == 0:
                print(screen)
                screen = []            

            if cycle % 40 == 20:
                #print(idx, cycle, register, (line, prev_add))
                signal_strength += cycle*register

            register += int(line.split(" ")[1])

print(signal_strength)