#!/usr/bin/env python

import sys

def parseInput():
    for line in sys.stdin:
        lines = line.strip().split(',')
        if len(lines)>1 and lines[0]!='VendorID':
            yield lines

def mapper():
    for lines in parseInput():
        total_amount = float(lines[18])
        pickup_time = lines[1]
        month = int(pickup_time.split('-')[1])
        if month < 4 :
            print "%s\t%s" % ('1', total_amount)
        elif month < 7 :
            print "%s\t%s" % ('2', total_amount)
        elif month < 10 :
            print "%s\t%s" % ('3', total_amount)
        elif month < 13 :
            print "%s\t%s" % ('4', total_amount)

if __name__=='__main__':
    mapper()