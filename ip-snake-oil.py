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
print('The IP entered was:')
print(ip)
print('\n')
print('The IP when converted to four octets is:')
print(octets)
print('\n')
print('The IP when converted into four binary objects is')
print(binary_octets)
print('\n')
print('When prepended with zeros so each octet is 8 chars long')
for octet in binary_octets:
    print(str(octet).zfill(8))
print('\n')
print('And finally the whole string in binary')
print(binary_whole_ip)
print('\n')
