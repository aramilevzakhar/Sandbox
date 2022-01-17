import sys
import socket
import threading
from  sock1 import Socket

s = Socket()




#socket.socket()
#s = socket.socket(family: socket.AF_INET, socket.SOCK_STREAM)
s = Server(socket.AF_INET, socket.SOCK_STREAM)


s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#host = '10.10.10.11'
host = socket.gethostname()

s.bind((host, 50007))

s.listen(5)
print('Server is listening')
users = []


def send_all(whose_msg, data):
    for user in users:
        if user != whose_msg:
            user.send(data)

def listen_server(user):
    while True:
        data = user.recv(2048)

        print(f'user sent {data}')
        send_all(user, data)

def start_server():
    while True:
        # set connections 
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!\n{clientsocket}")
        #clientsocket.send(bytes('Welcome to the server!', 'utf-8'))

        #data = clientsocket.recv(1024)
        

        #print(data.decode('utf-8'))
        users.append(clientsocket)
        threadslissen = threading.Thread(target=listen_server, args=(clientsocket,), daemon=True)
        threadslissen.start()

        #clientsocket.close()
        #clientsocket.close()

if __name__ == '__main__':
    #t = Socket()
    start_server()





