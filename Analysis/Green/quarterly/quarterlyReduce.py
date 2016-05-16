#!/usr/bin/env python

import sys

def processInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()
            yield line

def reducePhase():
    current_key = None
    current_amount = 0.0
    for line in processInput():
        month, amount = line.split('\t')
        try:
            amount = float(amount)
        except Exception:
            continue
        if current_key == month:
            current_amount += amount
        else:    
            if current_key:
                print '%s\t%s' % (current_key, current_amount)
            current_amount = amount
            current_key = month

    print '%s\t%s' % (current_key, current_amount)

if __name__=='__main__':
    reducePhase()