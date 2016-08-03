#!/usr/bin/env python

from netmiko import ConnectHandler
import getpass

sw1_pass = getpass.getpass(prompt = "Enter password for sw1: ")

pynet_sw1 = {
    'device_type': 'arista_eos',
    'ip':   '184.105.247.72',
    'username': 'admin1',
    'password': sw1_pass,
}

conf_vlan = ['conf t', 'vlan 255', 'name Test-Sahil']

#Method 1 - Using script
connect = ConnectHandler(**pynet_sw1)
output = connect.send_config_set(conf_vlan)
print "*" * 50
print "\nOutput: {}".format(output)

#Method 2 - Using file
connect = ConnectHandler(**pynet_sw1)
output = connect.send_config_from_file("config_file")
print "*" * 50
print "\nOutput: {}".format(output)
