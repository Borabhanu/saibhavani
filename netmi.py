from netmiko import ConnectHandler

with open('ip_list.txt') as routers:
    for IP in routers:

#First create the device object using a dictionary
        Router = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",

        }

# Next establish the SSH connection
        net_connect = ConnectHandler(**Router)
        print('connecting to ' + IP)
        print('_'*79)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('_'*79)
net_connect.disconnect()