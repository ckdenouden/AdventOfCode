import numpy as np
import math
import matplotlib.pyplot as plt

def get_nearby(x, y):
    return [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]

def get_closest(x_head, y_head, x_tail, y_tail):
    head = np.array([x_head, y_head])
    tail = np.array([x_tail, y_tail])

    head_close = [(x_head-1, y_head), (x_head+1, y_head), (x_head, y_head-1), (x_head, y_head+1)]
    min_dist = math.dist(tail, head)
    min_pos = tail
    for pos in head_close:
        dist = math.dist(tail, pos)
        if dist < min_dist:
            min_dist = dist
            min_pos = pos
    return min_pos

def get_closest_v2(x_head, y_head, x_tail, y_tail):
    tail = np.array([x_tail, y_tail])

    head_close = [(x_head-1, y_head), (x_head+1, y_head), (x_head, y_head-1), (x_head, y_head+1)]
    min_pos = tail
    options = []
    for pos in head_close:
        dist = math.dist(tail, pos)
        options.append(dist)
    minimum = np.min(options)
    if options.count(minimum) > 1:       
        tie = list(np.where(options == minimum)[0])
        if tie == [1, 3]:
            min_pos = (x_head+1, y_head+1)
        elif tie == [1, 2]:
            min_pos = (x_head+1, y_head-1)
        elif tie == [0, 2]:
            min_pos = (x_head-1, y_head-1)
        elif tie == [0, 3]:
            min_pos = (x_head-1, y_head+1)
        else:
            print(tie)
    else:
        min_pos = head_close[options.index(minimum)]
    
    return min_pos


dim = 1000
x_head, y_head = dim//2, dim//2
x_tail, y_tail = dim//2, dim//2
field = np.zeros((dim, dim), dtype=str)
with open("day09.txt", "r") as f:
    for idx, line in enumerate(f.readlines()):
        move, step = line.strip().split(" ")
    	
        for _ in range(int(step)):
            field[x_tail, y_tail] = "#"
            if move == "L":
                x_head -= 1
            elif move == "R":
                x_head += 1
            elif move == "U":
                y_head -= 1
            elif move == "D":
                y_head += 1
            
            head_nearby = get_nearby(x_head, y_head)
            if (x_tail, y_tail) not in head_nearby:
                x_tail, y_tail = get_closest(x_head, y_head, x_tail, y_tail)

visited = 0
for f in field.flatten():
    if f == "#":
        visited += 1
print(visited)





dim = 1000
field = np.zeros((dim, dim), dtype=str)
snake = [(dim//2, dim//2)]*10
with open("day09.txt", "r") as f:
    for idx, line in enumerate(f.readlines()):
        move, step = line.strip().split(" ")
    	
        for _ in range(int(step)):
            x_head, y_head = snake[0]
            x_tail, y_tail = snake[1]
            
            if move == "L":
                x_head -= 1
            elif move == "R":
                x_head += 1
            elif move == "U":
                y_head -= 1
            elif move == "D":
                y_head += 1
            
            head_nearby = get_nearby(x_head, y_head)
            if (x_tail, y_tail) not in head_nearby:
                x_tail, y_tail = get_closest(x_head, y_head, x_tail, y_tail)
            snake[0] = (x_head, y_head)
            snake[1] = (x_tail, y_tail)

            for s in range(1, len(snake)-1):
                x_head, y_head = snake[s]
                x_tail, y_tail = snake[s+1]

                if s == 8:
                    field[x_tail, y_tail] = "#"
                
                head_nearby = get_nearby(x_head, y_head)
                if (x_tail, y_tail) not in head_nearby:
                    x_tail, y_tail = get_closest_v2(x_head, y_head, x_tail, y_tail)
                
                snake[s+1] = (x_tail, y_tail)

visited = 0
for f in field.flatten():
    if f == "#":
        visited += 1
print(visited)