#!/usr/bin/env python

list = [40, 20, 10, 30, 50]
list.append(60)
list.append(70)
list.pop(0)

print "Length of list = {}".format(len(list))
list.sort()
print "Sorted list = {}".format(list) 
