#!/usr/bin/env python3
import sys
import re

trip_mode = False
route = None
boarded = 0
exited = 0
doors = 0

route_re = re.compile(r'^\s*route:\s*(\S+)', re.IGNORECASE)
board_re = re.compile(r'\bBOARD\b\s+(\d+)', re.IGNORECASE)
exit_re = re.compile(r'\bEXIT\b\s+(\d+)', re.IGNORECASE)
door_open_re = re.compile(r'\bDOOR_OPEN\b', re.IGNORECASE)
door_close_re = re.compile(r'\bDOOR_CLOSE\b', re.IGNORECASE)

def emit_current_trip():
    global route, boarded, exited, doors
    if route:
        print(f"{route}\t{boarded}|{exited}|{doors}")

def reset_trip():
    global route, boarded, exited, doors
    route = None
    boarded = 0
    exited = 0
    doors = 0

for raw in sys.stdin:
    line = raw.rstrip('\n')
    
    if 'TRIP_START' in line:
        trip_mode = True
        reset_trip()
        continue
    if 'TRIP_END' in line:
        emit_current_trip()
        trip_mode = False
        reset_trip()
        continue
    if not trip_mode:
        m = route_re.search(line)
        if m:
            route = m.group(1).strip()
        continue

    m = route_re.search(line)
    if m:
        route = m.group(1).strip()
        continue

    if board_re.search(line):
        m = board_re.search(line)
        boarded += int(m.group(1))

    if exit_re.search(line):
        m = exit_re.search(line)
        exited += int(m.group(1))

    if door_open_re.search(line) or door_close_re.search(line):
        doors += 1


if trip_mode:
    emit_current_trip()
