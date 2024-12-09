import numpy as np


f = [l.strip() for l in open("day08.txt", "r").readlines()]
f_arr = np.zeros((len(f[0]), len(f)), dtype=int)
for idx, row in enumerate(f):
    f_arr[idx] = [int(i)+1 for i in row]

f_arr_lr = f_arr.copy()
for row in range(f_arr.shape[0]):
    highest_lr = 0
    for col in range(f_arr.shape[1]):
        if f_arr[row, col] <= highest_lr:
            f_arr_lr[row, col] = 0
        else:
            highest_lr = f_arr[row, col]

f_arr_rl = f_arr.copy()
for row in range(f_arr.shape[0]):
    highest_rl = 0
    for col in reversed(range(f_arr.shape[1])):
        if f_arr[row, col] <= highest_rl:
            f_arr_rl[row, col] = 0
        else:
            highest_rl = f_arr[row, col]

f_arr_ud = f_arr.copy()
for col in range(f_arr.shape[1]):
    highest_ud = 0
    for row in range(f_arr.shape[0]):
        if f_arr[row, col] <= highest_ud:
            f_arr_ud[row, col] = 0
        else:
            highest_ud = f_arr[row, col]

f_arr_du = f_arr.copy()
for col in range(f_arr.shape[1]):
    highest_du = 0
    for row in reversed(range(f_arr.shape[0])):
        if f_arr[row, col] <= highest_du:
            f_arr_du[row, col] = 0
        else:
            highest_du = f_arr[row, col]

visible_all = f_arr_lr + f_arr_rl + f_arr_ud + f_arr_du
print("Number of visible trees:", np.count_nonzero(visible_all))


# Part 2
f_arr = np.zeros((len(f[0]), len(f)), dtype=int)
for idx, row in enumerate(f):
    f_arr[idx] = [int(i) for i in row]

maxscore = 0
for row in range(f_arr.shape[0]):
    for col in range(f_arr.shape[1]):
        self_len = f_arr[row, col]

        view_lr = f_arr[row, col+1:]
        view_rl = list(reversed(f_arr[row, :col]))
        view_ud = f_arr[row+1:, col]
        view_du = list(reversed(f_arr[:row, col]))
        if row == 0:
            view_du = []
        elif row == f_arr.shape[0]-1:
            view_ud = []
        elif col == 0:
            view_rl = []
        elif col == f_arr.shape[1]-1:
            view_lr = []

        visible_lr = 0
        for tree in view_lr:
            visible_lr += 1
            if tree >= self_len:
                break

        visible_rl = 0
        for tree in view_rl:
            visible_rl += 1
            if tree >= self_len:
                break

        visible_ud = 0
        for tree in view_ud:
            visible_ud += 1
            if tree >= self_len:
                break

        visible_du = 0
        for tree in view_du:
            visible_du += 1
            if tree >= self_len:
                break
        
        viewscore = visible_lr * visible_rl * visible_ud * visible_du
        if viewscore > maxscore:
            maxscore = viewscore
            coords = (row, col)

print("Best treehouse score:", maxscore)