#!/usr/bin/env python

def Function(x, y, z=20):
    return (x + y + z);

print "Sum: {}".format(Function(1, 5, 10))
print "Sum: {}".format(Function(x=1, y=5))
print "Sum: {}".format(Function(1, y=5, z=20))
print "Sum: {}".format(Function('I', 'am', 'Groot'))
print "Sum: {}".format(Function([1], [5], [100]))
