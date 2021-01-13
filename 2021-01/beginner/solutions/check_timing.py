#!/usr/bin/env python

from __future__ import print_function
from traceback import print_exc
import sys

def parse_sta(lines):
    clk = {}
    for l in lines:
        l = l.strip()
        if "Type  :" in l:
            clk['type'] = l.split(":")[1].strip()
        elif "Slack" in l:
            if "No nets found" in l:
                continue
            if "Invalid clock" in l:
                continue
            try:
                clk['slack'] = float(l.split(":")[1])
            except Exception as e:
                print("Failed to parse slack line: ", l)
                print_exc()
        elif "TNS" in l:
            try:
                clk['tns'] = float(l.split(":")[1])
            except Exception as e:
                print("Failed to parse TNS line: ", l)
                print_exc()
        elif l == "":
            if clk: yield clk
            clk = {}
    if clk: yield clk

if __name__=="__main__":
    ret = 0
    with open(sys.argv[1]) as f:
        for c in parse_sta(f):
            if (c.has_key('slack') and c['slack'] < 0) or (c.has_key('tns') and c['tns'] < 0):
                print("Failed timing.", file=sys.stderr)
                print(c, file=sys.stderr)
                ret = -1
    if (ret>=0):
        print("All constrains are met.", file=sys.stderr)

    exit(ret) 
