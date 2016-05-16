#!/usr/bin/env python

import sys

def processInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()
            yield line

def reducePhase():
    current_week = None
    current_count = 0
    for line in processInput():
        week, count = line.split('\t')
        try:
            count = int(count)
        except Exception:
            continue
        if current_week == week:
            current_count += count
        else:    
            if current_week:
                print '%s\t%d' % (current_week, current_count)
            current_count = count
            current_week = week

    print '%s\t%d' % (current_week, current_count)

if __name__=='__main__':
    reducePhase()