import socket
import threading
import asyncio

host = socket.gethostname()
port = 50007              # The same port as used by the server
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(b'Hello, world')
#    data = s.recv(1024)
#print('Received', repr(data))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

async def inp(p):
    #x = threading.Thread(target=listen_server, args=(p,), daemon=True)
    #x.start()
    await asyncio.create_task(listen_server(5, 'hello'))
    while True:
        p.send(input(':::').encode('utf-8'))    

async def listen_server(user_socket):
    while True:
        #client.send(input(':::').encode('utf-8'))
        await asyncio.sleep(0.01)
        data = user_socket.recv(2048)
        print(data.decode('utf-8'))


#def send_server():
    




if __name__ == '__main__':
    asyncio.run(inp(client))
