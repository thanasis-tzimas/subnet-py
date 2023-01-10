# subnet-py
A simple subnetting tool written in Python.  
This tool is designed to take an IP address and a CIDR prefix and calculate the Netword Address, Start/End Address Range, Usable Start/End Addresses, Total Usable Hosts and the Broadcast Address. How it does it, it's explained in the next Chapter.

## Running examples
```sh
$ python3 subnet.py 20.10.20.10 13
Subnet Address: 20.10.20.10/13
Range of IP Addresses: 20.8.0.0 - 20.15.255.255
Usable IPs: 20.8.0.1 - 20.15.255.254
Hosts: 524286
Broadcast IP: 20.15.255.255
```

## How it does the calculations
* Start(First) Address of the Subnet:  
The start address is calculated by doing a bitwise AND operation between the given IP address and the CIDR Subnet Mask.  
`ip & masks[cidr]` in line `47` in the code.  

* End(Last/Broadcast) Address of the Subnet:  
This is a tricky calculation, but generaly, this address is calcuated by bitwise OR between the given IP address and the ones'(1s) complement of the CIDR Subnet Mask.   
**Disclaimer**: In Python, every default integer variable is regarded as a signed integer. This means that if you do ones' complement of an signed integer, the language will regarded as the signed complement of that number (which is either its negative/positive complement number). In Python you can work around this by either working with the `ctype` library or by doing an additional bitwise operation onto the inverted CIDR Subnet Mask. In this implementation, I chose to do the later, by bitwise AND between the inverted CIDR Subnet Mask and the number `0xffffffff`.  
`ip | (~masks[cidr] & 0xffffffff)` in line `48` in the code.  

* Start(First) Usable Address of the Subnet
This is calculated as: `Start Address + 1`  

* End(Last) Usable Address of the Subnet
This is calculated as: `Broadcast Address - 1`

* Total Host in Subnet  
This is calculated as: `2**(N [of bits in IPv4] - CIDR [prefix]) - 2 [Router and Broadcast IPs]`
