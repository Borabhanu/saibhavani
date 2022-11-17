from netmiko import ConnectHandler
 
#First create the device object using a dictionary
CSR = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345"
}
 
# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)
 
# Then send the command and print the output

# output1 = net_connect.send_command('show ip int brief')
# output2 = net_connect.send_command('show clock')
#output3 = net_connect.send_command('show ip ro')
#output = net_connect.send_command('show run')
hostname = net_connect.send_command('show run | i host')

# print (output1)
# print (output2)
#print (output3)
print (hostname)
 
# Finally close the connection
net_connect.disconnect()