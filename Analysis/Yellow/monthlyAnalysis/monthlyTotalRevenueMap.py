#!/usr/bin/env python

import sys

def processInput():
    for lines in sys.stdin:
        lines = lines.strip()
        values = lines.split(',')
        if len(values)>1 and values[0]!='VendorID':
            yield values

def mappingPhase():
    for values in processInput():
        total_amount = float(values[18])
        pickup_time = values[1]
        month = pickup_time.split('-')[1]
        print "%s\t%s" % (month, total_amount)

if __name__=='__main__':
    mappingPhase()
