#!/usr/bin/env python

def OpenFile(filename):
    with open(filename) as file:
        return(file.read());

def FindVendor(output):
    for line in output.splitlines():
        if 'IOS Software' in line:
            vendor, _ = line.split("IOS Software")
    return vendor

def FindModelNumber(output):
    for line in output.splitlines():
        if 'processor' in line:
            model, _ = line.split("processor")
    return model

def FindOSVersion(output):
    for line in output.splitlines():
        if 'Version' in line:
            if 'Bootstrap' in line:
                continue
            else:
                _, version_temp = line.split("Version")
                for word in version_temp.splitlines():
                    version, _ = word.split(", RELEASE")
    return version

def FindSerialNumber(output):
    for line in output.splitlines():
        if 'Processor board ID' in line:
            _, serial_number = line.split("Processor board ID")
    return serial_number

def FindUptime(output):
    for line in output.splitlines():
        if 'uptime' in line:
            _, uptime = line.split("uptime is")
    return uptime

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
