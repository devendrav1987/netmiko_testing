#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import os
from netmiko import ConnectHandler
from getpass import getpass


a_user = os.environ.get("userw")
b_passw = os.environ.get("passw")
c_host = os.environ.get("hostw")
print(c_host)
print(a_user)
print(b_passw)

cisco1 = { 
    "device_type": "cisco_ios",
    "host": c_host,
    "username": a_user,
    "password": b_passw,
}

# Show command that we execute.
command = "show ip int brief"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()
with open("test.txt", 'w+', encoding='utf-8') as f:
    f.write(output)
