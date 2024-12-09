import regex as re

# Part 1
numsum_1 = 0
with open("01.txt", "r") as f:
    for line in f.readlines():
        line = line.strip("\n")
        matches = re.findall(r"(\d)", line)
        number = matches[0] + matches[-1]
        numsum_1 += int(number)
print(numsum_1)

# Part 2
s_to_d = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
numsum_2 = 0
with open("01.txt", "r") as f:
    for line in f.readlines():
        line = line.strip("\n")
        regex_str = "|".join(f"({k})" for k in s_to_d.keys())
        matches = [[n for n in m if n][0] for m in re.findall(f"(\d)|{regex_str}", line, overlapped=True)]
        if matches[0].isdigit():
            first = matches[0]
        else:
            first = s_to_d[matches[0]]
        if matches[-1].isdigit():
            last = matches[-1]
        else:
            last = s_to_d[matches[-1]]
        number = first + last
        # print(number)
        numsum_2 += int(number)
print(numsum_2)
