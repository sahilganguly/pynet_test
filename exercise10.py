#!/usr/bin/env python

output = open("exercise10_output.txt", "w")
output.write("{:20} {:50}\n".format("Prefix", "AS Path"))

with open("show_ip_bgp.txt") as file:
    for line in file.readlines():
        for i, word in enumerate(line.split()):
            if word == '*' and i == 0 :
                prefix = line.split()[1]
                aspath = line.split()[5:]
                aspath.pop()
                aspath = ' '.join(aspath)
                output.write("{:20} {:50}\n".format(prefix, aspath))

output.close()                
