import socket
import threading
import asyncio
import time


host = socket.gethostname()
port = 50007              # The same port as used by the server
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(b'Hello, world')
#    data = s.recv(1024)
#print('Received', repr(data))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def start_input(name_user, socket_handler):
    x = threading.Thread(target=listen_server, args=(socket_handler,), daemon=True)
    x.start()
    #await asyncio.create_task(listen_server(5, 'hello'))
    while True:
        time.sleep(1)
        p.send(input(f'{name_user}: ').encode('utf-8'))    

def listen_server(user_socket):
    while True:
        #client.send(input(':::').encode('utf-8'))
        #await asyncio.sleep(0.01)
        data = user_socket.recv(2048)
        print(data.decode('utf-8'))
    

if __name__ == '__main__':
    my_name = input('Type your name: ')

    try:
        start_input(my_name, client)
    except Exception:
        #except KeyboardInterrupt ^ ConnectionResetError:
        print("hello")


    #asyncio.run(inp(client))
    
