monkeys_num = dict()
monkeys_ops = dict()
with open("day21.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip().split(": ")
        try:
            monkeys_num.update({line[0]: int(line[1])})
        except ValueError:
            monkeys_ops.update({line[0]: line[1]})

while len(monkeys_ops) > 0:
    monkeys_done = []
    for monkey_name, monkey_task in monkeys_ops.items():
        monkey_n1, monkey_op, monkey_n2 = monkey_task.split(" ")        
        try:
            monkey_n1_val = monkeys_num[monkey_n1]
            monkey_n2_val = monkeys_num[monkey_n2]
            monkey_answer = eval(" ".join([str(monkey_n1_val), monkey_op, str(monkey_n2_val)]))
            monkeys_num.update({monkey_name: monkey_answer})
            monkeys_done.append(monkey_name)
        except KeyError:
            continue
    [monkeys_ops.pop(m) for m in monkeys_done]
print(monkeys_num["root"])


monkeys_num = dict()
monkeys_ops = dict()
with open("day21.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip().split(": ")
        if line[0] == "humn":
            monkeys_ops.update({line[0]: None})
        try:
            monkeys_num.update({line[0]: int(line[1])})
        except ValueError:
            monkeys_ops.update({line[0]: line[1]})

monkeys_humn = []
new_humn = False
reduced = False
while len(monkeys_ops) > 0:
    monkeys_done = []
    for monkey_name, monkey_task in monkeys_ops.items():
        if monkey_name == "humn":
            if monkey_name not in monkeys_humn:
                monkeys_humn.append("humn")
                new_humn = True
            continue
        monkey_n1, monkey_op, monkey_n2 = monkey_task.split(" ")
        if (monkey_n1 in monkeys_humn or monkey_n2 in monkeys_humn):
            if monkey_name not in monkeys_humn:
                monkeys_humn.append(monkey_name)
                new_humn = True
            continue
        try:
            monkey_n1_val = monkeys_num[monkey_n1]
            monkey_n2_val = monkeys_num[monkey_n2]
            monkey_answer = eval(" ".join([str(monkey_n1_val), monkey_op, str(monkey_n2_val)]))
            monkeys_num.update({monkey_name: monkey_answer})
            monkeys_done.append(monkey_name)
            reduced = True
        except KeyError:
            continue
    [monkeys_ops.pop(m) for m in monkeys_done]
    if not new_humn and not reduced:
        monkey_n1, monkey_op, monkey_n2 = monkeys_ops["root"].split(" ")
        monkey_n1_val = monkeys_num[monkey_n2]
        monkeys_num.update({monkey_n1: monkey_n1_val})
        for h in range(2,len(monkeys_humn)):
            h_curr = monkeys_humn[-h]
            h_prev = monkeys_humn[-h-1]
            monkey_n1, monkey_op, monkey_n2 = monkeys_ops[h_curr].split(" ")
            if h_prev == monkey_n1:
                if monkey_op == "+":
                    monkey_n1_val = monkeys_num[h_curr] - monkeys_num[monkey_n2]
                elif monkey_op == "-":
                    monkey_n1_val = monkeys_num[h_curr] + monkeys_num[monkey_n2]
                elif monkey_op == "*":
                    monkey_n1_val = monkeys_num[h_curr] / monkeys_num[monkey_n2]
                elif monkey_op == "/":
                    monkey_n1_val = monkeys_num[h_curr] * monkeys_num[monkey_n2]
                monkeys_num.update({monkey_n1: monkey_n1_val})
            elif h_prev == monkey_n2:
                if monkey_op == "+":
                    monkey_n2_val = monkeys_num[h_curr] - monkeys_num[monkey_n1]
                elif monkey_op == "-":
                    monkey_n2_val = monkeys_num[monkey_n1] - monkeys_num[h_curr]
                elif monkey_op == "*":
                    monkey_n2_val = monkeys_num[h_curr] / monkeys_num[monkey_n1]
                elif monkey_op == "/":
                    monkey_n2_val = monkeys_num[monkey_n1] / monkeys_num[h_curr]
                monkeys_num.update({monkey_n2: monkey_n2_val})
        print(monkeys_num["humn"])
        break
    new_humn = False
    reduced = False