#!/usr/bin/env python3
import sys

def expected_hcode(temp, co2, hum):
    temp_flag = temp > 28
    co2_flag = co2 > 2000
    hum_flag = hum < 25

    flags = temp_flag + co2_flag + hum_flag

    if flags == 0:
        return "H0"
    if flags == 1:
        if temp_flag:
            return "H1"
        if co2_flag:
            return "H2"
        if hum_flag:
            return "H3"
    return "H4"

for raw in sys.stdin:
    line = raw.strip()
    parts = [p.strip() for p in line.split("|")]

    timestamp, building, sensor, temp, co2, hum, reported = parts

    try:
        temp = float(temp)
        co2 = float(co2)
        hum = float(hum)
    except:
        continue

    expected = expected_hcode(temp, co2, hum)
    reported = reported.upper()
    match = 1 if expected == reported else 0
    print(f"{building}|{sensor}\t1|{match}")
