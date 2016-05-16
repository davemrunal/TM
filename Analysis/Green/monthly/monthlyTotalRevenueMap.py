#!/usr/bin/env python

import sys

def processInput():
    for lines in sys.stdin:
        lines = lines.strip().split(',')
        if len(lines)>1 and lines[0]!='VendorID':
            yield lines

def mappingPhase():
    for lines in processInput():
        total_amount = float(lines[18])
        pickup_time = lines[1]
        month = pickup_time.split('-')[1]
        print "%s\t%s" % (month, total_amount)

if __name__=='__main__':
    mappingPhase()