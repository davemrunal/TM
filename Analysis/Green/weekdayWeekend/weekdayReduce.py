#!/usr/bin/env python

import sys

def processInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()
            yield line

def reducePhase():
    current_week = None
    current_amount = 0.0
    for line in processInput():
        week, amount = line.split('\t')
        try:
            amount = float(amount)
        except Exception:
            continue
        if current_week == week:
            current_amount += amount
        else:
            if current_week:
                print '%s\t%s' % (current_week, current_amount)
            current_amount = amount
            current_week = week

    print '%s\t%s' % (current_week, current_amount)

if __name__=='__main__':
    reducePhase()