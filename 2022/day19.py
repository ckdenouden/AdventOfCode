import functools
import time
import re


blueprints = []
with open("day19.txt", "r") as f:
    for line in f.readlines():
        bpid, ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_obsidian = [int(i) for i in re.findall(r'\d+', line)]
        blueprints.append((bpid, (ore_cost, clay_cost, (obsidian_cost_ore, obsidian_cost_clay), (geode_cost_ore, geode_cost_obsidian))))

@functools.cache
def minute(bp, M, m=1, resources=(0, 0, 0, 0), robots=(1, 0, 0, 0), building=""):
    cost_ore = bp[0]
    cost_clay = bp[1]
    cost_obsidian = bp[2]
    cost_geode = bp[3]
    cost_highest_ore = max(cost_ore, cost_clay, cost_obsidian[0], cost_geode[0])

    max_geodes = 0
    ore, clay, obsidian, geode = resources
    r_ore, r_clay, r_obsidian, r_geode = robots

    ore += r_ore
    clay += r_clay
    obsidian += r_obsidian
    geode += r_geode

    if m == M:
        return geode

    if building == "ore":
        ore -= cost_ore
        r_ore += 1
    elif building == "clay":
        ore -= cost_clay
        r_clay += 1
    elif building == "obsidian":
        ore -= cost_obsidian[0]
        clay -= cost_obsidian[1]
        r_obsidian += 1
    elif building == "geode":
        ore -= cost_geode[0]
        obsidian -= cost_geode[1]
        r_geode += 1
    

    ore = min(ore, (cost_highest_ore-r_ore)*(M-m)+r_ore)
    clay = min(clay, (cost_obsidian[1]-r_clay)*(M-m)+r_clay)
    r_ore_sat = True if r_ore >= cost_highest_ore or ore >= cost_highest_ore*(M-m) else False
    r_clay_sat = True if r_clay >= cost_obsidian[1] or clay >= cost_obsidian[1]*(M-m)else False
    r_obsidian_sat = True if r_obsidian >= cost_geode[1] or obsidian >= cost_geode[1]*(M-m) else False

    options = [""]
    if ore >= cost_ore and not r_ore_sat:
        options.append("ore")
    if ore >= cost_clay and not r_clay_sat:
        options.append("clay")
    if ore >= cost_obsidian[0] and clay >= cost_obsidian[1] and not r_obsidian_sat:
        options.append("obsidian")
    if ore >= cost_geode[0] and obsidian >= cost_geode[1]:
        options = ["geode"]
    
    m += 1
    for o in options:
        resources = (ore, clay, obsidian, geode)
        robots = (r_ore, r_clay, r_obsidian, r_geode)
        max_geodes = max(max_geodes, minute(bp, M, m, resources, robots, building=o))
    #print(max_geodes, m, robots, resources)
    
    return max_geodes


agg = 0
MINUTES = 24
for blueprint in blueprints:
    start = time.time()
    bpid = blueprint[0]
    geodes = minute(blueprint[1], MINUTES)
    print(bpid, geodes, time.time()-start)
    agg += blueprint[0] * geodes
print(agg)


agg = 1
MINUTES = 32
for blueprint in blueprints[:3]:
    start = time.time()
    bpid = blueprint[0]
    geodes = minute(blueprint[1], MINUTES)
    print(bpid, geodes, time.time()-start)
    agg *= geodes
print(agg)