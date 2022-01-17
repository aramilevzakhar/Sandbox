import socket


#class Server(socket.socket):
#    def __init__(self, AF_INET, SOCK_STREAM):
#        super().__init__(socket.AF_INET, socket.SOCK_STREAM)



#class Server(socket.socket):
#    def __init__(self, AF_INET, SOCK_STREAM):
#        self.family = AF_INET
#        self.proto = AF_INET


class Server(socket.socket):
    def __init__(self, AF_INET, SOCK_STREAM):
        socket.socket.__init__(self, socket.AF_INET, socket.SOCK_STREAM)

















