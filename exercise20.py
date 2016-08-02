#!/usr/bin/env python
import re

def OpenFile(filename):
    with open(filename) as file:
        return(file.read());

def FindVendor(output):
    match = re.search(r"(.*) IOS Software *", output)
    if match:
        return match.group(1)

def FindModelNumber(output):
    match = re.search(r"(.*) processor \(*", output)
    if match:
        return match.group(1)

def FindOSVersion(output):
    match = re.search(r"Cisco IOS Software.* Version (.*), .*", output)
    if match:
        return match.group(1)

def FindSerialNumber(output):
    match = re.search(r"Processor board ID (.*)", output)
    if match:
        return match.group(1)

def FindUptime(output):
    match = re.search(r".* uptime is (.*)", output)
    if match:
        return match.group(1)

output = OpenFile("show_version.txt")
vendor = FindVendor(output)
model = FindModelNumber(output)
version = FindOSVersion(output)
serial_number = FindSerialNumber(output)
uptime = FindUptime(output)

dict = {'Vendor': vendor, 'Model': model, 'Version': version, 'Serial Number': serial_number, 'Uptime': uptime}
print "{:20} {:20}".format("Key", "Value")
print "{:20} {:20}".format("===", "=====")
for k, v in dict.items():
    print "{:20} {:20}".format(k, v)
