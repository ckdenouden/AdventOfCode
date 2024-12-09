import matplotlib.pyplot as plt

elves = []
with open("day23.txt", "r") as f:
    y = 0
    for line in f.readlines():
        line = line.strip()
        for c in range(len(line)):
            if line[c] == "#":
                elves.append((c,y))
        y += 1


ROUNDS = 10000
directions = [((0, -1), (1, -1), (-1, -1)), ((0, 1), (1, 1), (-1, 1)), ((-1, 0), (-1, -1), (-1, 1)), ((1, 0), (1, -1), (1, 1))]
directions_set = set()
[[directions_set.add(_d) for _d in d] for d in directions]
for round in range(1, ROUNDS+1):
    proposals = []
    for elf in elves:
        elf_clear = True
        for direction in directions_set:
            elf_new = tuple([sum(x) for x in zip(elf, direction)])
            if elf_new in elves:
                elf_clear = False
                break
        if elf_clear:
            proposal = elf
        else:
            for idx_d, direction in enumerate(directions):
                elf_clear = True
                for idx_sd, subdirection in enumerate(direction):
                    elf_new = tuple([sum(x) for x in zip(elf, subdirection)])
                    if elf_new in elves:
                        elf_clear = False
                        break
                if elf_clear:
                    proposal = tuple([sum(x) for x in zip(elf, direction[0])])
                    break
                elif idx_d == 3:
                    proposal = elf
        proposals.append(proposal)

    elves_new = []
    for idx, elf in enumerate(elves):
        proposal = proposals[idx]
        if proposals.count(proposal) == 1:
            elves_new.append(proposal)
        else:
            elves_new.append(elf)
    if elves == elves_new:
        print("No one moved in round", round) # 1040
        break
    elves = elves_new
    
    if round == 10:
        elf_xmin = 0
        elf_xmin = min([elf[0] for elf in elves])
        elf_xmax = max([elf[0] for elf in elves])
        elf_ymin = min([elf[1] for elf in elves])
        elf_ymax = max([elf[1] for elf in elves])
        empty = ((elf_xmax-elf_xmin+1)*(elf_ymax-elf_ymin+1)) - len(elves)
        print(empty)

    directions = directions[1:] + [directions[0]]