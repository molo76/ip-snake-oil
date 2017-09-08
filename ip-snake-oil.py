## Python3 script for getting info about an IP/CIDR

# Get some user input
y = input('Enter an IP address with CIDR mask, for example 10.100.23.1/24:\n')

# Split the ip from the mask
ip,mask = y.split('/')

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
print('The IP entered was:\t\t\t\t' + ip)

# Moving onto the subnet mask, get the 'network bits' portion of the mask:
network_bits = int(mask) * '1'

# Get the host bits portion of the mask:
host_bits = (32 - int(mask)) * '0'

# Create the whole mask in binary:
mask_bits = network_bits + host_bits

# Now cut into 4 octets and turn into binary (not actually used anywhere in the script at present, so commented out)
#mask_binary_octets = []
#mask_binary_octets.append(mask_bits[0:7])
#mask_binary_octets.append(mask_bits[8:15])
#mask_binary_octets.append(mask_bits[16:23])
#mask_binary_octets.append(mask_bits[24:31])

# Create dotted decimal subnet mask string
subnet_mask = str(int(mask_bits[0:8], 2)) + '.' + str(int(mask_bits[8:16], 2)) + '.' + str(int(mask_bits[16:24], 2)) + '.' + str(int(mask_bits[24:32], 2))

print('The subnet mask is:\t\t\t\t' + subnet_mask)

# Now need to find the first & last host plus broadcast address. 

# Turn host_bits (current binary zeros) to binary 1's for calculating number of available host IPs
# Join found from StackOverflow - need to spend some more time learning this useful tool 
# Explanation & examples here: https://www.tutorialspoint.com/python/string_join.htm
# Found that I don't actually need this to work out the number of hosts. 
# host_bits_inverted = ''.join('1' if x == '0' else '0' for x in host_bits)


# Print the number of host IP's available:
host_network_mask = '1' + host_bits
print('Number of IPs in the subnet:\t\t\t' + str(int(host_network_mask, 2)))
print('Number of host IPs available in this network:\t' + str(int(host_network_mask, 2) - 2))

# Find interesting octet (network/host) boundary in subnet_mask: 
for octet in subnet_mask_octets:
    if octet != '255':
       print(octet)
       int_subnet_octet = subnet_mask_octets.index(octet)
       break




