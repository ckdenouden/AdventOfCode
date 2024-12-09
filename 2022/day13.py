import ast


def is_ordered(l):
    left = l[0]
    right = l[1]

    for i in range(max(len(left), len(right))):
        empty_left, empty_right = False, False
        try:
            ileft = left[i]
        except IndexError:
            empty_left = True
        
        try:
            iright = right[i]
        except IndexError:
            empty_right = True
        
        if empty_left and empty_right:
            return None
        elif empty_left:
            return True
        elif empty_right:
            return False
        
        if type(ileft) == int and type(iright) == int:
            if ileft > iright:
                ordered = False
            elif ileft < iright:
                ordered = True
            else:
                continue
        elif type(ileft) == list and type(iright) == list:
            ordered = is_ordered([ileft, iright])
            if ordered is None:
                continue
        elif type(ileft) == list and type(iright) == int:
            ordered = is_ordered([ileft, [iright]])
            if ordered is None:
                continue
        elif type(ileft) == int and type(iright) == list:
            ordered = is_ordered([[ileft], iright])
            if ordered is None:
                continue
        
        return ordered
    return None


order = []
with open("day13.txt", "r") as f:
    lines = f.readlines()
    for idx in range(len(lines)-1):
        if lines[idx] == "\n" or lines[idx+1] == "\n":
            continue
        line_1 = lines[idx].strip()
        line_2 = lines[idx+1].strip()
        linelist_1 = ast.literal_eval(line_1)
        linelist_2 = ast.literal_eval(line_2)
        ordered = is_ordered([linelist_1, linelist_2])
        order.append(ordered)
correctly_ordered = [i+1 for i in range(len(order)) if order[i]]
print("Sum of correctly ordered:", sum(correctly_ordered))


changed = True
with open("day13.txt", "r") as f:
    lines = [ast.literal_eval(l.strip()) for l in f.readlines() if l != "\n"]
    lines.append([[2]])
    lines.append([[6]])
    while changed:
        changed = False
        for idx in range(len(lines)-1):
            line_1 = lines[idx]
            line_2 = lines[idx+1]
            isordered = is_ordered([line_1, line_2])
            if isordered == False:
                lines[idx] = line_2
                lines[idx+1] = line_1
                changed = True
print("Decoder indices:", lines.index([[2]])+1, lines.index([[6]])+1)
print("Decoder key:", (lines.index([[2]])+1)*(lines.index([[6]])+1))
