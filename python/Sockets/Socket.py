import socket


class Server(socket.socket):
    def __init__(self, host, port, number):
        self.bind(host, port)
        self.listen(number)
        print('Server is listening')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)













