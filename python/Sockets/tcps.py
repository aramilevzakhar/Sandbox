import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 9999))







server.listen()

while True:
    client, addr = server.accept()
    print(f'Connected to {addr}')
    print(client.recv(1024).decode('utf-8'))
    client.send('Hello client!'.encode('utf-8'))

    print(client.recv(1024).decode('utf-8'))
    client.send('Buy!'.encode('utf-8'))
    client.close()





