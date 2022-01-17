import socket


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


client.sendto("hello server 1".encode('utf-8'), (socket.gethostname(), 9999))
print(client.recvfrom(1024)[0].decode('utf-8'))

client.sendto("hello server 2".encode('utf-8'), (socket.gethostname(), 9999))
print(client.recvfrom(1024)[0].decode('utf-8'))













