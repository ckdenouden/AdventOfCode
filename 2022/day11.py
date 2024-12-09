import math
import numpy as np
import time


def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


class Monkey():
    def __init__(self, name, items, operation, test, istrue, isfalse) -> None:
        self.name = name.lower()
        self.items = items
        self.operation = operation
        self.test = test
        self.istrue = istrue
        self.isfalse = isfalse

    def count_items(self):
        return len(self.items)

    def process_item(self):
        old = self.items.pop(0)
        exec("global new; " + self.operation)
        new_relief = new % lcm #math.floor(new / 3)
        passed = (new_relief % self.test == 0)
        if passed:
            return new_relief, self.istrue
        else:
            return new_relief, self.isfalse

    def add_item(self, item):
        self.items.append(item)

monkeys = []
monkey_divisors = []
with open("day11.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if "Monkey" in line:
            m_name = line[:-1]
        elif "Starting items" in line:
            m_items = [int(i.strip()) for i in line.split(":")[1].split(",")]
        elif "Operation" in line:
            m_operation = line.split(":")[1].strip()
        elif "Test" in line:
            m_test = int(line.split(":")[1].split(" ")[-1])
            monkey_divisors.append(m_test)
        elif "If true" in line:
            m_istrue = int(line.split(":")[1].split(" ")[-1])
        elif "If false" in line:
            m_isfalse = int(line.split(":")[1].split(" ")[-1])
            monkeys.append(Monkey(m_name, m_items, m_operation, m_test, m_istrue, m_isfalse))

from math import gcd
lcm = 1
for i in monkey_divisors:
    lcm = lcm*i//gcd(lcm, i)

rounds = 10000
inspections = np.zeros(len(monkeys), dtype=np.int64)
for round in range(rounds):
    for m in range(len(monkeys)):
        monkey = monkeys[m]
        n_items = monkey.count_items()
        inspections[m] += n_items
        for _ in range(n_items):
            item, receiver = monkey.process_item()
            monkeys[receiver].add_item(item)

print("Inspections:", inspections)
monkey_business = np.prod(sorted(inspections)[-2:])
print("Monkey business:", monkey_business)
