#!/usr/bin/env python

with open("show_version.txt") as file:
    for line in file.readlines():
        for i, word in enumerate(line.split()):
            if word == 'ID':
                serial = line.split()[i+1]
    print "Serial number: {}".format(serial)
