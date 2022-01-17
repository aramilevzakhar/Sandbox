
import socket
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '10.10.10.11'
host = socket.gethostname()

s.bind((host, 50007))

s.listen(5)
print('Server is listening')
users = []


def send_all(data):
    for user in users:
        user.send(data)

class Socket(socket.socket):
    def __init__(self):
        super().__init__()
socket.socket()    



def listen_server(user):
    while True:
        data = user.recv(2048)
        print(f'user sent {data}')
        send_all(data)

def start_server():
    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        #clientsocket.send(bytes('Welcome to the server!', 'utf-8'))

        #data = clientsocket.recv(1024)
        #print(data.decode('utf-8'))
        users.append(clientsocket)
        threadslissen = threading.Thread(target=listen_server, args=(clientsocket,), daemon=True)
        threadslissen.start()

        #clientsocket.close()
        #clientsocket.close()

if __name__ == '__main__':
    t = Socket()

    start_server()





