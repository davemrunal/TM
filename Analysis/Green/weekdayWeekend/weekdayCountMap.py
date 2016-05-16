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
        pickup_datetime = value[1]
        date = datetime.strptime(pickup_datetime,"%Y-%m-%d %H:%M:%S")
        day=date.weekday()
        if day<5:
            print "Week%d Weekdays\t%d" % (date.isocalendar()[1], 1)
        else:
            print "Week%d Weekend\t%d" % (date.isocalendar()[1], 1)

if __name__=='__main__':
    mappingPhase()