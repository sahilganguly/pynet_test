#!/usr/bin/env python
ip = raw_input("Enter an IP address: ")
octets = ip.split(".")
octets[-1] = 0
octets2 = []

for i in octets:
    octets2.append(bin(int(i)))
print "\n{:12} {:12} {:12} {:12}".format("Octet1", "Octet2", "Octet3", "Octet4")
print "\n{:12} {:12} {:12} {:12}".format(*octets)
print "\n{:12} {:12} {:12} {:12}".format(*octets2)
