#!/usr/bin/env python

from __future__ import print_function
from traceback import print_exc
from datetime import datetime
import sys

def l2v(l, index=-2):
    return float(l.split()[index])

def parse_entry(entry):
    dt = datetime.strptime(entry[0], "%a %b %d %H:%M:%S %Y")
    volts = l2v(entry[2])
    amps = l2v(entry[3])
    inlet_temp = l2v(entry[6], -3)
    local_temp = l2v(entry[7], -3)
    core_temp = l2v(entry[8], -3)
    return (dt, volts, amps, volts*amps, inlet_temp, local_temp, core_temp)

def parse_log(lines):
    entry = []
    for l in lines:
        if "ERROR" in l.decode("utf-8"):
            print(l)
            continue
        entry +=  [l.decode("utf-8").strip()]
        if len(entry) == 9:
            yield parse_entry(entry)
            entry = []
    if entry:
        print("log ends with partial entry: ", entry)

if __name__=="__main__":
    with open(sys.argv[1]) as f:
        for c in parse_log(f):
            print(c)

