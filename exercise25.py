#!/usr/bin/env python

from netmiko import ConnectHandler
import getpass

rtr1_pass = getpass.getpass(prompt = "Enter password for rtr1: ")
sw1_pass = getpass.getpass(prompt = "Enter password for sw1: ")

pynet_rtr1 = {
    'device_type': 'cisco_ios',
    'ip':   '184.105.247.70',
    'username': 'pyclass',
    'password': rtr1_pass,
}

pynet_sw1 = {
    'device_type': 'arista_eos',
    'ip':   '184.105.247.72',
    'username': 'admin1',
    'password': sw1_pass,
}

connect = ConnectHandler(**pynet_rtr1)
print "Current Prompt: {}".format(connect.find_prompt())
show_ver = connect.send_command('show version')
print "*" * 50
print "\nShow Version Output: {}".format(show_ver)
show_run = connect.send_command('show run')
print "*" * 50
print "\nShow Running Output: {}".format(show_run)

with open("rtr1_show_ver", "w") as file:
    file.write(show_run)

connect = ConnectHandler(**pynet_sw1)
print "Current Prompt: {}".format(connect.find_prompt())
show_ver = connect.send_command('show version')
print "*" * 50
print "\nShow Version Output: {}".format(show_ver)
show_run = connect.send_command('show run')
print "*" * 50
print "\nShow Running Output: {}".format(show_run)

with open("sw1_show_ver", "w") as file:
    file.write(show_run)
