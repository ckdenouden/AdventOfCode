
with open("day06.txt", "r") as f:
    signal = f.readline().strip()

first_sop, first_som = 4, 14
check_sop, check_som = True, True
for step in range(len(signal)):
    chunk_sop = signal[step:step+4]
    chunk_som = signal[step:step+14]
    if len(set(chunk_sop)) == 4 and check_sop:
        print("First sop marker after character", first_sop)
        check_sop = False
    if len(set(chunk_som)) == 14 and check_som:
        print("First som marker after character", first_som)    
        check_som = False
    first_sop += 1
    first_som += 1
