#!/usr/bin/env python3
import sys

current_route = None
total_boarded = 0
total_exited = 0
total_doors = 0

def emit(route, boarded, exited, doors):
    total_passengers = boarded + exited
    if doors == 0:
        ratio = 0.0
    else:
        ratio = total_passengers / doors
    status = "ACCEPT" if ratio >= 1.0 else "REJECT"
    print(f"{route}, {total_passengers}, {doors}, {ratio:.2f}, {status}")

for raw in sys.stdin:
    line = raw.strip()
    route, vals = line.split("\t", 1)
    parts = vals.split("|")

    b = int(parts[0])
    e = int(parts[1])
    d = int(parts[2])
    
    if current_route is None:
        current_route = route
        total_boarded = b
        total_exited = e
        total_doors = d
    elif route == current_route:
        total_boarded += b
        total_exited += e
        total_doors += d
    else:
        emit(current_route, total_boarded, total_exited, total_doors)
        current_route = route
        total_boarded = b
        total_exited = e
        total_doors = d

if current_route is not None:
    emit(current_route, total_boarded, total_exited, total_doors)
