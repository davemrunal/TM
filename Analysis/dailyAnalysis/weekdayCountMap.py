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
        pickup_datetime = value[1]
        date = datetime.strptime(pickup_datetime,"%Y-%m-%d %H:%M:%S")
        d=date.weekday()
        if d<5:
            print "%s\t%s" % ('Week'+str(date.isocalendar()[1])+' Weekdays', '1')
        else:
            print "%s\t%s" % ('Week'+str(date.isocalendar()[1])+' Weekend', '1')

if __name__=='__main__':
    mappingPhase()
