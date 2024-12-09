def get_priority(char):
    if char.islower():
        priority = ord(char) - 96
    elif char.isupper():
        priority = ord(char) - 38
    return priority


common_sum = 0
badge_sum = 0
with open("day03.txt", "r") as f:
    members = 0
    for line in f.readlines():
        line = line.strip()
        compartment_1 = line[:len(line)//2]
        compartment_2 = line[len(line)//2:]
        common = list(set(compartment_1) & set(compartment_2))[0]
        common_sum += get_priority(common)

        if members == 0:
            members_common = set(line)
        else:
            members_common = list(set(members_common) & set(line))
        members += 1

        if members == 3:
            badge = members_common[0]
            badge_sum += get_priority(badge)
            members = 0

print(common_sum)
print(badge_sum)