#!/usr/bin/env python

import sys

def processInput():
    for lines in sys.stdin:
        lines = lines.strip().split(',')
        if len(lines)>1 and lines[0]!='VendorID':
            yield lines

def mappingPhase():
    for value in processInput():
        total_amount = float(value[18])
        pickup_datetime = value[1]
        month = pickup_datetime.split('-')[1]
        if total_amount < 0 :
            print "%s\t%s" % (month,total_amount)

if __name__=='__main__':
    mappingPhase()