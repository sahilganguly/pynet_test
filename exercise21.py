#!/usr/bin/env python
import re

def OpenFile(filename):
    with open(filename) as file:
        return(file.read());

class Device:
    
    def __init__(self, output):
        self.output = output
        self.vendor = ''
        self.model = ''
        self.version = ''
        self.serial_number = ''
        self.uptime = ''

    def FindVendor(self):
        match = re.search(r"(.*) IOS Software *", output)
        if match:
           self.vendor = match.group(1)

    def FindModelNumber(self):
        match = re.search(r"(.*) processor \(*", output)
        if match:
            self.model = match.group(1)

    def FindOSVersion(self):
        match = re.search(r"Cisco IOS Software.* Version (.*), .*", output)
        if match:
            self.version = match.group(1)

    def FindSerialNumber(self):
        match = re.search(r"Processor board ID (.*)", output)
        if match:
            self.serial_number = match.group(1)

    def FindUptime(self):
        match = re.search(r".* uptime is (.*)", output)
        if match:
            self.uptime = match.group(1)

output = OpenFile("show_version.txt")

deviceobject = Device(output)
deviceobject.FindVendor()
deviceobject.FindModelNumber()
deviceobject.FindOSVersion()
deviceobject.FindSerialNumber()
deviceobject.FindUptime()

print "Vendor: {}".format(deviceobject.vendor)
print "Model: {}".format(deviceobject.model)
print "OS Version: {}".format(deviceobject.version)
print "Serial Number: {}".format(deviceobject.serial_number)
print "Uptime: {}".format(deviceobject.uptime)
