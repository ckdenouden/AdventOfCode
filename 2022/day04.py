full_overlap = 0
any_overlap = 0
with open("day04.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        #print(line)
        elf_1, elf_2 = line.split(",")
        elf_1_start, elf_1_stop = [int(x) for x in elf_1.split("-")]
        elf_2_start, elf_2_stop = [int(x) for x in elf_2.split("-")]
        elf_1_range = set(range(elf_1_start, elf_1_stop+1))
        elf_2_range = set(range(elf_2_start, elf_2_stop+1))
        elf_innerjoin = elf_1_range & elf_2_range
        if elf_innerjoin == elf_1_range or elf_innerjoin == elf_2_range:
            full_overlap += 1
        if elf_innerjoin != set():
            any_overlap += 1
        
print("Full overlap:", full_overlap)
print("Any overlap:", any_overlap)