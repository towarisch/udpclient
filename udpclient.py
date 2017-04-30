import socket

target_host = "www.google.de"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n", (target_host, target_port))
data, addr = client.recvfrom(4096)
print data