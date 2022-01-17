import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((socket.gethostname(), 9999))

while True:
    message, addr = server.recvfrom(1024)
    print(addr)
    print(message.decode('utf-8'))

    server.sendto('hello client! 1'.encode('utf-8'), addr)
    print(server.recvfrom(1024)[0].decode('utf-8'), addr)

    server.sendto('hello client! 2'.encode('utf-8'), addr)








