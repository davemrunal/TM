#!/usr/bin/env python

import sys
from datetime import datetime

def processInput():
    for lines in sys.stdin:
        lines = lines.strip()
        values = lines.split(',')
        if len(values)>1 and values[0]!='VendorID':
            yield values

def mappingPhase():
    for value in processInput():
        total_amount=float(value[18])
        pickup_datetime = value[1]
        date = datetime.strptime(pickup_datetime,"%Y-%m-%d %H:%M:%S")
        d=date.weekday()
        if d<5:
            print "Week%s Weekdays\t%s" % (date.isocalendar()[1], total_amount)
        else:
            print "Week%s Weekend\t%s" % (date.isocalendar()[1], total_amount)

if __name__=='__main__':
    mappingPhase()
