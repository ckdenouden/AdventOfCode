def snafu2dec(snafu):
    dec = 0
    for idx, c in enumerate(snafu):
        if c == "-":
            c = -1
        elif c == "=":
            c = -2

        dec += int(c) * 5**(len(snafu)-idx-1)
    return dec

def dec2snafu(dec):
    if dec == 0:
        return ""
    snafu_digits = ["2", "1", "0", "-", "="]
    div, mod = divmod(dec + 2, 5)
    tail = snafu_digits[4-mod]
    head = dec2snafu(div)
    return head + tail


with open("day25.txt", "r") as f:
    numsum = 0
    for line in f.readlines():
        snafu = line.rstrip()
        dec = snafu2dec(snafu)
        numsum += dec
    numsum_snafu = dec2snafu(numsum)
    print(numsum_snafu)