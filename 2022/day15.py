import numpy as np
import re

def manhattan_dist(source, signal):
    return abs(source[0]-signal[0])+abs(source[1]-signal[1])

def get_row_dist(source, dist, row):
    source_y = source[1]
    source_row_dist = abs(source_y-row)
    return max(dist-source_row_dist, 0)

beacons = []
impossible = []
probe_row = 10
with open("day15b.txt", "r") as f:
    for idx, line in enumerate(f.readlines()):
        line = line.strip()
        #print(idx, line)
        sensor_x = int(line.split(":")[0].split(",")[0][12:])
        sensor_y = int(line.split(":")[0].split(",")[1][3:])
        sensor = (sensor_x, sensor_y)
        #print(sensor)
        beacon_x = int(line.split(":")[1].split(",")[0][24:])
        beacon_y = int(line.split(":")[1].split(",")[1][3:])
        beacon = (beacon_x, beacon_y)
        beacons.append(beacon)
        dist = manhattan_dist(sensor, beacon)
        row_dist = get_row_dist(sensor, dist, probe_row)
        if row_dist > 0:
            for x in range(sensor[0]-row_dist, sensor[0]+row_dist+1):
                impossible.append((x, probe_row))
beacons = list(set(beacons))
impossible = list(set(impossible))

for b in beacons:
    try:
        del impossible[impossible.index(b)]
    except ValueError:
        continue
print("Row", probe_row, "has", len(impossible), "positions where the source cannot be.\n")

found = False
f = open("day15.txt", "r").read().split("\n")[:-1]
for probe_y in range(0, 4000001):    
    impossible = []
    for idx, line in enumerate(f):
        sensor_x = int(line.split(":")[0].split(",")[0][12:])
        sensor_y = int(line.split(":")[0].split(",")[1][3:])
        sensor = (sensor_x, sensor_y)
        beacon_x = int(line.split(":")[1].split(",")[0][24:])
        beacon_y = int(line.split(":")[1].split(",")[1][3:])
        beacon = (beacon_x, beacon_y)
        dist = manhattan_dist(sensor, beacon)
        row_dist = get_row_dist(sensor, dist, probe_y)
        if row_dist > 0:
            impossible.append((max(sensor[0]-row_dist, 0), min(sensor[0]+row_dist+1, 4000001)))
    
    impossible = sorted(impossible)
    range_max = impossible[0][1]
    for r in impossible:
        if r[0] > range_max:
            x_coords = [i[0] for i in impossible]
            probe_x = r[0]-1
            print("Distress beacon found at:", probe_x, probe_y)
            print("Tuning frequency:", 4000000*probe_x + probe_y)
            found = True
            break
        elif r[1] > range_max:
            range_max = r[1]
    if found:
        break



