from sys import argv
from socket import inet_ntoa
masks = {
        0:  0x00000000,
        1:  0x80000000,
        2:  0xc0000000,
        3:  0xe0000000,
        4:  0xf0000000,
        5:  0xf8000000,
        6:  0xfc000000,
        7:  0xfe000000,
        8:  0xff000000,
        9:  0xff800000,
        10: 0xffc00000,
        11: 0xffe00000,
        12: 0xfff00000,
        13: 0xfff80000,
        14: 0xfffc0000,
        15: 0xfffe0000,
        16: 0xffff0000,
        17: 0xffff8000,
        18: 0xffffc000,
        19: 0xffffe000,
        20: 0xfffff000,
        21: 0xfffff800,
        22: 0xfffffc00,
        23: 0xfffffe00,
        24: 0xffffff00,
        25: 0xffffff80,
        26: 0xffffffc0,
        27: 0xffffffe0,
        28: 0xfffffff0,
        29: 0xfffffff8,
        30: 0xfffffffc,
        31: 0xfffffffe,
        32: 0xffffffff
}

ipv4 = argv[1].split('.')
cidr = int(argv[2], base = 10)

ip = 0x0
i = 3
for octet in ipv4:
    ip += int(octet, base = 10) * 0x100 ** i
    i -= 1
start_ip = inet_ntoa((ip & masks[cidr]).to_bytes(4, 'big'))
end_ip = inet_ntoa((ip | (~masks[cidr] & 0xffffffff)).to_bytes(4, 'big'))
start_usable = inet_ntoa(((ip & masks[cidr]) + 1).to_bytes(4, 'big'))
end_usable = inet_ntoa(((ip | (~masks[cidr] & 0xffffffff)) - 1).to_bytes(4, 'big'))
broadcast_ip = end_usable
ip = inet_ntoa(ip.to_bytes(4, 'big'))

print(f'Subnet Address: {ip}/{cidr}')
print(f'Range of IP Addresses: {start_ip} - {end_ip}')
print(f'Usable IPs: {start_usable} - {end_usable}')
print(f'Hosts: {2**(32 - cidr)-2}')
print(f'Broadcast IP: {broadcast_ip}')
