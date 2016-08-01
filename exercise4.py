#!/usr/bin/env python
ip = raw_input("Enter an IP address: ")
octets = ip.split(".")
print "\n{:12} {:12} {:12} {:12}".format(*octets)
