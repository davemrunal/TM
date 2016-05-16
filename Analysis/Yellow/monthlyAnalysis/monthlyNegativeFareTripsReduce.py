#!/usr/bin/env python
import sys

def processInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()
            yield line

def reducePhase():
    current_key = None
    current_count = 0
    for line in processInput():
        month, count = line.split('\t')
        try:
            count = int(count)
        except Exception:
            continue
        if current_key == month:
            current_count += count
        else:    
            if current_key:
                print '%s\t%s' % (current_key, current_count)
            current_count = count
            current_key = month

    if current_key == month:
        print '%s\t%s' % (current_key, current_count)

if __name__=='__main__':
    reducePhase()
