# ip-snake-oil
A script to disassemble an IP/CIDR string and display relevant information. 

Enter a string, for example 192.168.0.100/24. The script will output the following: 

* IP address: 192.168.0.100
* Subnet Mask: 255.255.255.0
* Network address: 192.168.0.0
* Broadcast address: 192.168.0.255
* Number of IPs in the subnet: 256
* Number of host IPs available: 254

Python3 based. 

##### Sept 13th 2017 #####
Completed subnet mask work. Script outputs as expected. No user input validation yet. 

##### Sept 4th 2017 #####
Working on sections to convert IP to binary values and to convert CIDR to binary and dotted decimal mask. 
