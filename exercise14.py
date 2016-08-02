#!/usr/bin/env python

network_device = {'ip_address': '4.2.2.2', 'username': 'admin', 'password': 'boxboxbox', 'vendor': 'Arista', 'model': 'DCS-7050'}

print "{:20} {:20}".format("Key", "Value")
for k, v in network_device.items():
    print "{:20} {:20}".format(k, v)

network_device['password'] = 'boxboxboxbox'
network_device['secret'] = 'supersecretsquirrel'

device_type = network_device.get('device_type', 'Cisco IOS')
print "\nDevice type: {}".format(device_type)
