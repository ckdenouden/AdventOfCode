import functools
import itertools
import re
from collections import defaultdict as ddict


valves = set()
rates = dict()
distances = ddict(lambda: 10**9)
with open("day16.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        v_name = line[6:8]
        v_rate = int(line.split(";")[0].split("=")[1])
        v_conn = re.search(r'valves? (.+)$', line).group(1).split(", ")

        valves.add(v_name)
        if v_rate > 0:
            rates[v_name] = v_rate
        for c_name in v_conn:
            distances[v_name, c_name] = 1

for x, i, j in itertools.product(valves, valves, valves):
    distances[i,j] = min(distances[i,x] + distances[x,j], distances[i,j])

@functools.cache
def traverse(valve1, t, unvisited):
    valverates = [0]
    if unvisited != frozenset():
        for valve2 in unvisited:
            if distances[valve1, valve2] < t:
                t_new = t - distances[valve1, valve2] - 1
                valverates.append(rates[valve2] * t_new + traverse(valve1=valve2, t=t_new, unvisited=unvisited-{valve2}))
    return max(valverates)
print(traverse(valve1="AA", t=30, unvisited=frozenset(rates)))

@functools.cache
def traverse_elephant(valve1, t, unvisited):
    valverates = [traverse(valve1="AA", t=26, unvisited=unvisited)]
    if unvisited != frozenset():
        for valve2 in unvisited:
            if distances[valve1, valve2] < t:
                t_new = t - distances[valve1, valve2] - 1
                valverates.append(rates[valve2] * t_new + traverse_elephant(valve1=valve2, t=t_new, unvisited=unvisited-{valve2}))
    return max(valverates)
print(traverse_elephant(valve1="AA", t=26, unvisited=frozenset(rates)))