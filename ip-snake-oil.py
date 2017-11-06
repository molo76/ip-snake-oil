## Python3 script for getting info about an IP/CIDR
import sys
import re

#
if len (sys.argv) < 1:
    # Get some user input
    print('\n')
    y = input('Enter an IP address with CIDR mask, for example 10.100.23.1/24:\n')
if len (sys.argv) == 1:
    y = (sys.argv[1])

######################
## Input validation ##
######################

# Regex to match expected string, if not true end script
regex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}")
if not regex.match(y):
    sys.exit("aa! errors! please enter IP/mask in the correct format!")

# Split the ip from the mask
ip,mask = y.split('/')

################
## Work on IP ##
################

# Take the 4 octets from the IP and add them to a list called 'octets'
octets = ip.split('.')

# Create an empty list called 'binary_octets', to hold the binary version of each octet
binary_octets = []

# Loop through the 4 octets and turn each one into binary, then store into the 'binary_octets' list
for octet in octets:
    binary_octets.append(int(bin(int(octet))[2:]))

# Create an empty string called 'binary_whole_ip'
binary_whole_ip = ''

# Add the four binary octets from the binary_octets list into one string 'binary_whole_ip', ensuring each one is padded with zeros to make it 8 chars in length
for octet in binary_octets:
     binary_whole_ip+=str(octet).zfill(8)

# Now the ip address is stored as 4 integers in the octets list, as 4 binary numbers in the binary_octets list, and as a whole binary string in the binary_whole_ip variable:

print('\n')
print('IP address:\t\t\t' + ip)

##################
## Work on Mask ##
##################

# Moving onto the subnet mask, get the 'network bits' portion of the mask:
network_bits = int(mask) * '1'

# Get the host bits portion of the mask:
host_bits = (32 - int(mask)) * '0'

# Create the whole mask in binary:
mask_bits = network_bits + host_bits

# Create dotted decimal subnet mask string
subnet_mask = str(int(mask_bits[0:8], 2)) + '.' + str(int(mask_bits[8:16], 2)) + '.' + str(int(mask_bits[16:24], 2)) + '.' + str(int(mask_bits[24:32], 2))
print('Subnet Mask:\t\t\t' + subnet_mask)

# First IP (network address) in binary:
network_binary = binary_whole_ip[0:int(mask)] + host_bits
# Convert to dotted decimal notation:
network_ip = str(int(network_binary[0:8], 2)) + '.' + str(int(network_binary[8:16], 2)) + '.' + str(int(network_binary[16:24], 2)) + '.' + str(int(network_binary[24:32], 2))

# Last IP (broadcast address) in binary:
# Invert host_bits first, from zeros to ones:
host_bits_inverted = ''.join('1' if x == '0' else '0' for x in host_bits)
broadcast_binary = binary_whole_ip[0:int(mask)] + host_bits_inverted
# Convert to dotted decimal notation:
broadcast_ip = str(int(broadcast_binary[0:8], 2)) + '.' + str(int(broadcast_binary[8:16], 2)) + '.' + str(int(broadcast_binary[16:24], 2)) + '.' + str(int(broadcast_binary[24:32], 2))

print('Network address:\t\t' + network_ip)
print('Broadcast address:\t\t' + broadcast_ip)

# Print the number of host IP's available:
host_network_mask = '1' + host_bits
print('Number of IPs in the subnet:\t' + str(int(host_network_mask, 2)))
print('Number of host IPs available:\t' + str(int(host_network_mask, 2) - 2))
print('\n')
