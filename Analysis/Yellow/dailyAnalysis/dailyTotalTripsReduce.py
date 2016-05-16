#!/usr/bin/env python
import itertools, operator, sys

def processInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducePhase():
    for key, values in itertools.groupby(processInput(), operator.itemgetter(0)):
        count = sum(map(int, zip(*values)[1]))
        print '%s\t%s' % (key, count)

if __name__=='__main__':
    reducePhase()
