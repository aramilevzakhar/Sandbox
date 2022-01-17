import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((socket.gethostname(), 9999))

client.send("Hello server!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))

client.send('Buy!'.encode('utf-8'))
print(client.recv(1024).decode('utf-8'))







