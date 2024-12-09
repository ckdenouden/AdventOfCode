import numpy as np
import time

rock_1 = np.array((
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 1]),
    dtype=int
)
rock_2 = np.array((
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0]),
    dtype=int
)
rock_3 = np.array((
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 1, 1, 0]),
    dtype=int
)
rock_4 = np.array((
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0]),
    dtype=int
)
rock_5 = np.array((
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0]),
    dtype=int
)

rocks = [np.fliplr(r.T) for r in [rock_1, rock_2, rock_3, rock_4, rock_5]]
jets = [c for c in open("day17.txt", "r").read().strip()]
shaft = np.zeros((7, 10000), dtype=int)

rock_anchor = (2, 3)
idx_r = 0
idx_j = 0
rock_count = 0

shaft_growth = []
shaft_length = 0

while True:
    if rock_count == 5000:
        break

    rock = rocks[idx_r]
    jet = jets[idx_j]

    if jet == "<":
        space = shaft[rock_anchor[0]-1:rock_anchor[0]+3, rock_anchor[1]:rock_anchor[1]+4]

        if space.shape != (4, 4) and rock_anchor[0] == 0:
            space = np.concatenate([np.ones((1, 4), dtype=int), space])
        elif space.shape != (4, 4):
            space = np.concatenate([space, np.ones((4-space.shape[0], 4), dtype=int)])

        if np.sum(rock * space) == 0:
            rock_anchor = (rock_anchor[0]-1, rock_anchor[1])
            #print("Moved rock", rock_count, "left", rock_anchor)
        else:
            #print("Rock", rock_count, "couldn't move left", rock_anchor)
            pass
        
    elif jet == ">":
        space = shaft[rock_anchor[0]+1:rock_anchor[0]+5, rock_anchor[1]:rock_anchor[1]+4]
        if space.shape != (4, 4):
            
            space = np.concatenate([space, np.ones((4-space.shape[0], 4), dtype=int)])
        if np.sum(rock * space) == 0:
            rock_anchor = (rock_anchor[0]+1, rock_anchor[1])
            #print("Moved rock", rock_count, "right", rock_anchor)
        else:
            #print("Rock", rock_count, "couldn't move right", rock_anchor)
            pass
    
    space = shaft[rock_anchor[0]:rock_anchor[0]+4, rock_anchor[1]-1:rock_anchor[1]+3]
    if space.shape[0] != 4:
        space = np.concatenate([space, np.ones((4-space.shape[0], 4), dtype=int)])


    if space.shape == (4, 4) and np.sum(rock * space) == 0:
        rock_anchor = (rock_anchor[0], rock_anchor[1]-1)
        #print("Moved rock", rock_count, "down", rock_anchor)
    else:
        #print("Rock", rock_count, "couldn't move down")
        if rock_anchor[0] > 3:
            shaft[rock_anchor[0]:rock_anchor[0]+4, rock_anchor[1]:rock_anchor[1]+4] += rock[:-max(rock_anchor[0]-3, 1), :]
        else:
            shaft[rock_anchor[0]:rock_anchor[0]+4, rock_anchor[1]:rock_anchor[1]+4] += rock
        idx_r += 1
        idx_r %= len(rocks)
        max_shaft = max((shaft>0).nonzero()[1])+1
        shaft_growth.append(max_shaft-shaft_length)
        shaft_length = max_shaft
        rock_anchor = (2, max((shaft>0).nonzero()[1])+4)
        rock_count += 1


    idx_j += 1
    idx_j %= len(jets)


#print("Tower of rocks is", 50*shifted + max((shaft>0).nonzero()[1])+1, "units tall.")
print("Tower of rocks is", max_shaft, "units tall.")

def find_repeat(data):
    for start in range(500):
        for window in range(10, 2000):
            window1 = data[start:start+window]
            window2 = data[start+window:start+2*window]
            if window1 == window2:
                return start, window
repeat_start, repeat_window = find_repeat(shaft_growth)
warmup = shaft_growth[:repeat_start]
warmup_height = sum(warmup)
repeats = (1000000000000-repeat_start) // repeat_window
repeats_height = repeats * sum(shaft_growth[repeat_start:repeat_start+repeat_window])
remainder = (1000000000000-repeat_start) % repeat_window
remainder_height = sum(shaft_growth[repeat_start:repeat_start+remainder])
total_height = warmup_height + repeats_height + remainder_height
print("Tower of rocks is", total_height, "units tall.")