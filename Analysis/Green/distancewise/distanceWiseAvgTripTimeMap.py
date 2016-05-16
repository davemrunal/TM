#!/usr/bin/env python

import sys
from datetime import datetime

def processInput():
    for lines in sys.stdin:
        lines = lines.strip().split(',')
        if len(lines)>1 and lines[0]!='VendorID':
            yield lines

def mappingPhase():
    for value in processInput():
        pickupickupDateateTime=datetime.strptime(value[1],'%Y-%m-%d %H:%M:%S')
        dropoffDateTime=datetime.strptime(value[2],'%Y-%m-%d %H:%M:%S')
        travelTime=int((dropoffDateTime-pickupickupDateateTime).total_seconds())
        distance=float(value[10])
        pickupDate=value[1].strip().split()[0]
        if distance<11:
            print "%s,Short\t%d" % (pickupDate,travelTime)
        elif distance<21:
            print "%s,Medium\t%d" % (pickupDate,travelTime)
        else:
            print "%s,Long\t%d" % (pickupDate,travelTime)

if __name__=='__main__':
    mappingPhase()