#!/usr/bin/env python3
import sys

current_key = None
total = 0
matched = 0

def emit(key, total, matched):
    building, sensor = key.split("|")
    rate = (matched / total) * 100 if total > 0 else 0
    status = "OK" if rate >= 85 else "Faulty"
    print(f"{building}, {sensor}, {rate:.2f}%, {status}")

for raw in sys.stdin:
    line = raw.strip()

    key, vals = line.split("\t")
    cnt, m = vals.split("|")
    cnt = int(cnt)
    m = int(m)

    if current_key is None:
        current_key = key
        total = cnt
        matched = m
    elif key == current_key:
        total += cnt
        matched += m
    else:
        emit(current_key, total, matched)
        current_key = key
        total = cnt
        matched = m

if current_key is not None:
    emit(current_key, total, matched)
