### Part 1
# Example
with open("2024/data/09_example.txt", "r") as f:
    disk = f.readlines()
    disk = [[int(l2) for l2 in l1.strip()] for l1 in disk][0]

# uncompress disk
disk_uncompressed = []
file_id = 0
for file, file_length in enumerate(disk):
    if file % 2 == 0:
        disk_uncompressed.append([file_id] * file_length)
        file_id += 1
    else:
        disk_uncompressed.append([None] * file_length)
disk_uncompressed = sum(disk_uncompressed, [])

# consolidate disk
disk_consolidated = disk_uncompressed.copy()
disk_stripped = [d for d in disk_consolidated if d is not None]
disk_stripped_len = len(disk_stripped)
for idx, file in enumerate(disk_consolidated):
    if file is None:
        disk_consolidated[idx] = disk_stripped.pop()
disk_consolidated = disk_consolidated[:disk_stripped_len]

# calculate checksum
disk_checksum = 0
for pos, file_id in enumerate(disk_consolidated):
    disk_checksum += pos * file_id
print("Example 1:", disk_checksum)

# Puzzle
with open("2024/data/09_input.txt", "r") as f:
    disk = f.readlines()
    disk = [[int(l2) for l2 in l1.strip()] for l1 in disk][0]

# uncompress disk
disk_uncompressed = []
file_id = 0
for file, file_length in enumerate(disk):
    if file % 2 == 0:
        disk_uncompressed.append([file_id] * file_length)
        file_id += 1
    else:
        disk_uncompressed.append([None] * file_length)
disk_uncompressed = sum(disk_uncompressed, [])

# consolidate disk
disk_consolidated = disk_uncompressed.copy()
disk_stripped = [d for d in disk_consolidated if d is not None]
disk_stripped_len = len(disk_stripped)
for idx, file in enumerate(disk_consolidated):
    if file is None:
        disk_consolidated[idx] = disk_stripped.pop()
disk_consolidated = disk_consolidated[:disk_stripped_len]

# calculate checksum
disk_checksum = 0
for pos, file_id in enumerate(disk_consolidated):
    disk_checksum += pos * file_id
print("Puzzle 1:", disk_checksum)


### Part 2
# Example
with open("2024/data/09_example.txt", "r") as f:
    disk = f.readlines()
    disk = [[int(l2) for l2 in l1.strip()] for l1 in disk][0]

# uncompress disk
disk_uncompressed = []
file_id = 0
for file, file_length in enumerate(disk):
    if file % 2 == 0:
        disk_uncompressed.append([file_id] * file_length)
        file_id += 1
    else:
        disk_uncompressed.append([None] * file_length)
disk_uncompressed = [d for d in disk_uncompressed if d]

# consolidate disk
disk_consolidated = disk_uncompressed.copy()
for block_id in reversed(range(max([d for d in sum(disk_consolidated, []) if d]) + 1)):
    for move_idx, move in enumerate(reversed(disk_consolidated)):
        if block_id in move:
            move_idx = len(disk_consolidated) - move_idx - 1
            break

    for file_idx, file in enumerate(disk_consolidated):
        if None in file and file_idx < move_idx and len(file) > len(move):
            disk_consolidated[move_idx] = [None] * len(move)
            disk_consolidated[file_idx] = move
            disk_consolidated.insert(file_idx + 1, [None] * (len(file) - len(move)))
            break
        elif None in file and file_idx < move_idx and len(file) == len(move):
            disk_consolidated[move_idx] = [None] * len(move)
            disk_consolidated[file_idx] = move
            break
disk_consolidated = sum(disk_consolidated, [])

# calculate checksum
disk_checksum = 0
for pos, file_id in enumerate(disk_consolidated):
    if file_id is not None:
        disk_checksum += pos * file_id
print("Example 2:", disk_checksum)

# Puzzle
with open("2024/data/09_input.txt", "r") as f:
    disk = f.readlines()
    disk = [[int(l2) for l2 in l1.strip()] for l1 in disk][0]

# uncompress disk
disk_uncompressed = []
file_id = 0
for file, file_length in enumerate(disk):
    if file % 2 == 0:
        disk_uncompressed.append([file_id] * file_length)
        file_id += 1
    else:
        disk_uncompressed.append([None] * file_length)
disk_uncompressed = [d for d in disk_uncompressed if d]

# consolidate disk
disk_consolidated = disk_uncompressed.copy()
for block_id in reversed(range(max([d for d in sum(disk_consolidated, []) if d]) + 1)):
    for move_idx, move in enumerate(reversed(disk_consolidated)):
        if block_id in move:
            move_idx = len(disk_consolidated) - move_idx - 1
            break

    for file_idx, file in enumerate(disk_consolidated):
        if None in file and file_idx < move_idx and len(file) > len(move):
            disk_consolidated[move_idx] = [None] * len(move)
            disk_consolidated[file_idx] = move
            disk_consolidated.insert(file_idx + 1, [None] * (len(file) - len(move)))
            break
        elif None in file and file_idx < move_idx and len(file) == len(move):
            disk_consolidated[move_idx] = [None] * len(move)
            disk_consolidated[file_idx] = move
            break
disk_consolidated = sum(disk_consolidated, [])

# calculate checksum
disk_checksum = 0
for pos, file_id in enumerate(disk_consolidated):
    if file_id is not None:
        disk_checksum += pos * file_id
print("Puzzle 2:", disk_checksum)
