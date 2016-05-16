#!/usr/bin/env python

import sys

def processInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()
            yield line

def reducePhase():
    curr_distance = None
    curr_sum = 0
    curr_count = 0
    for line in processInput():
        key, value = line.split('\t')
        try:
            value = int(value)
        except Exception:
            continue
        if curr_distance == key:
            curr_sum += value
            curr_count += 1
        else:    
            if curr_distance:
                print '%s\t%d' % (curr_distance, curr_sum/curr_count)
            curr_sum = value
            curr_distance = key
            curr_count = 1

    print '%s\t%d' % (curr_distance, curr_sum/curr_count)

if __name__=='__main__':
    reducePhase()