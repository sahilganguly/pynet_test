#!/usr/bin/env python

def OpenFile(filename):
    with open(filename) as file:
        return(file.read());

def FindSerialNumber(output):
    for line in output.splitlines():
        if 'Processor board ID' in line:
            x, serial_number = line.split("Processor board ID")
    return serial_number

output = OpenFile("show_version.txt")
print "Serial number: {}".format(FindSerialNumber(output))
