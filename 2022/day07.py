files = []
with open("day07.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")

        if line[0] == "$":
            cmd = line.split(" ")[1:]
            if cmd[0] == "cd":
                if cmd[1] == "/":
                    cwd = "/"
                elif cmd[1] == "..":
                    cwd = "/".join(cwd.split("/")[:-2]) + "/"
                else:
                    cwd += cmd[1] + "/"
        
        elif line.split(" ")[0] != "dir":
            filepath = cwd + line.split(" ")[1]
            filesize = int(line.split(" ")[0])
            files.append((filepath, filesize))
pathsum = dict()
for f in files:
    f_filepath, f_size = f
    f_filepath_split = f_filepath.split("/")
    for l in range(len(f_filepath_split)-1):
        f_path = "/".join(f_filepath_split[:-l-1])
        if f_path in pathsum.keys():
            pathsum.update({f_path: pathsum[f_path]+f_size})
        else:
            pathsum.update({f_path: f_size})

v_sum = 0
for k, v in pathsum.items():
    if v < 100000:
        v_sum += v
print(v_sum)

required_space = 30000000 - (70000000 - pathsum[""])
pathsum_sorted = {k: v for k, v in sorted(pathsum.items(), key=lambda item: item[1])}

for k, v in pathsum_sorted.items():
    if v >= required_space:
        print(v)
        break
        