# Sockets & Packets
**Explore:** [Home](/README.md) [Basics](/0-Basics.md)

## Encoding

### Hex
```bash
echo "Message" | xxd -p                             # Encode text to Hex
xxd file.txt file-encoded.txt                       # Encode file to Hex
xxd -r file-encoded.txt file-decoded.txt            # Decode file from Hex
```

```py
import binascii
message = b'Message'
hidden_msg = binascii.hexlify(message)
new_msg = binascii.unhexlify(hidden_msg)
```

### Base64
```bash
echo "Message" | base64                             # Encode text to base64
base64 file.txt > file-encoded.txt                  # Endode file to Base64
base64 -d file-encoded.txt > file-decoded.txt       # Decode file from Base64
```

```py
import base64
message = b'Message'
hidden_msg = base64.b64encode(message)
new_msg = base64.b64decode(hidden_msg)
```

## TCP Stream Socket

### Sender
```py
#!/usr/bin/python3
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
ip_addr = '127.0.0.1'
port = 1111
s.connect((ip_addr, port))
message = b"Message"
s.send(message)
data, conn = s.recvfrom(1024)
print(data.decode('utf-8'))
s.close()
```

### Receiver
```py
#!/usr/bin/python3
import socket
import os
port = 1111
message = b"Connected to TCP Server on port %i\n" % port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port))
s.listen(1)
os.system("clear")
print ("Waiting for TCP connections\n")
while 1:
    conn, addr = s.accept()
    connect = conn.recv(1024)
    address, port = addr
    print ("Message Received - '%s'" % connect.decode())
    print ("Sent by -", address, "port -", port, "\n")
    conn.sendall(message)
    conn.close()
```

## UDP Datagram Socket

### Sender
```py
#!/usr/bin/python3
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
ip_addr = '127.0.0.1'
port = 2222
message = b"Message"
s.sendto(message, (ip_addr, port))
data, addr = s.recvfrom(1024)
print(data.decode())
s.close()
```

### Receiver
```py
#!/usr/bin/python3
import socket
import os
port = 2222
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
s.bind(('', port))
os.system("clear")
print ("Awaiting UDP Messages")
while True:
    data, addr = s.recvfrom(1024)
    address, port = addr
    print ("\nMessage Received: '%s'" % data.decode())
    print ("Sent by -", address, "port", port)
    s.sendto(b"Message received by the UDP Message Server!", addr)
```

## Raw Sockets

### IP
```py
#!/usr/bin/python3
import sys
import socket
from struct import pack
import base64
import binascii

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print(msg)
    sys.exit()

packet = ''
src_ip = "127.0.0.1" 
dst_ip = "127.0.0.1" 

#####################
##  Packet Header  ##
#####################
# Normally 0x45 for Version and Internet Header Length
ip_ver_ihl = 0x45
ip_tos = 24 << 2                # E.g. shift 2 for DSCP pos
ip_len = 0
ip_id = 1984
ip_frag = 0
ip_ttl = 64
ip_proto = 16                   # CHAOS
ip_check = 0

ip_srcadd = socket.inet_aton(src_ip)
ip_dstadd = socket.inet_aton(dst_ip)

ip_header = pack('!BBHHHBBH4s4s' , ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_srcadd, ip_dstadd)

#############
## Message ##
#############

message = b'MESSAGE'
hidden_msg = binascii.hexlify(message)

packet = ip_header + hidden_msg
s.sendto(packet, (dst_ip, 0))
```

### TCP

```py
#!/usr/bin/python3
import array
import socket
import sys
from struct import pack
import base64
import binascii

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print(msg)
    sys.exit()

src_ip = "127.0.0.1"
dst_ip = "127.0.0.1"

################################
### Build IPv4 Packet Header ###
################################
ip_ver_ihl = 0x45
ip_tos = 0
ip_len = 0
ip_id = 2020
ip_frag = 0
ip_ttl = 64
ip_proto = 6
ip_check = 0
ip_srcadd = socket.inet_aton(src_ip)
ip_dstadd = socket.inet_aton(dst_ip)

ip_header = pack('!BBHHHBBH4s4s' , ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_srcadd, ip_dstadd)

##########################
###  Build TCP Header  ###
##########################
tcp_src = 54321
tcp_dst = 1234
tcp_seq = 90210
tcp_ack_seq = 30905
#tcp_off_res =
tcp_data_off = 5
tcp_reserve = 0
tcp_off_res = (tcp_data_off << 4) + tcp_reserve

tcp_flags = 0b0000_0010
# tcp_fin = 0                    # Finished
# tcp_syn = 0                    # Synchronization
# tcp_rst = 0                    # Reset
# tcp_psh = 0                    # Push
# tcp_ack = 0                    # Acknowledgement
# tcp_urg = 0                    # Urgent
# tcp_ece = 0                    # Explicit Congestion Notification Echo
# tcp_cwr = 0                    # Congestion Window Reduced

# tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh << 3) + (tcp_ack << 4) + (tcp_urg << 5) + (tcp_ece << 6) + (tcp_cwr << 7)
tcp_win = 65535
tcp_chk = 0
tcp_urg_ptr = 0

tcp_hdr = pack('!HHLLBBHHH', tcp_src, tcp_dst, tcp_seq, tcp_ack_seq, tcp_off_res, tcp_flags, tcp_win, tcp_chk, tcp_urg_ptr)


message = b'MESSAGE'
hidden_msg = base64.b64encode(message)

# After creating tcp header, create pseudo header for tcp checksum

src_address = socket.inet_aton(src_ip)
dst_address = socket.inet_aton(dst_ip)
reserved = 0
protocol = socket.IPPROTO_TCP
tcp_length = len(tcp_hdr) + len(hidden_msg)

ps_hdr = pack('!4s4sBBH', src_address, dst_address, reserved, protocol, tcp_length)
ps_hdr = ps_hdr + tcp_hdr + hidden_msg

def checksum(data):
        if len(data) % 2 != 0:
                data += b'\0'
        res = sum(array.array("H", data))
        res = (res >> 16) + (res & 0xffff)
        res += res >> 16
        return (~res) & 0xffff

tcp_chk = checksum(ps_hdr)

tcp_hdr = pack('!HHLLBBH', tcp_src, tcp_dst, tcp_seq, tcp_ack_seq, tcp_off_res, tcp_flags, tcp_win) + pack('H', tcp_chk) + pack('!H', tcp_urg_ptr)

packet = ip_header + tcp_hdr + hidden_msg

# s.connect((dst_ip, port))
# s.send(packet)

s.sendto(packet, (dst_ip, 0))
```
