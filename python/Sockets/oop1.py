import socket

HEADSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:

    clientsocket, address = s.accept()
    print(f'Connection from {address} has been estabilished!')

    msg = 'Welcome to the server!'
    msg = f'{len(msg):<{HEADSIZE}}' + msg

    clientsocket.send(bytes('Welcome to the server!', 'utf-8'))
    clientsocket.close()














