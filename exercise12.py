#!/usr/bin/env python
import os

network = raw_input("Please enter a /24 network: ")
network = network.split(".")
i_network = network[:]

for i in range(1,11):
    value = int(network[-1]) + i
    value = str(value)
    i_network[-1] = value
    ip = '.'.join(i_network)
    value = os.system("ping -c 1 -w 1 " + ip + " > /dev/null")
    if value == 0:
        print "{} is up".format(ip)
