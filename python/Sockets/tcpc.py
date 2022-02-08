import socket
import threading
import time
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((socket.gethostname(), 6666))



def listen(client):
    msg1 = 0
    acc = 0
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
        except:
            print('Error')
            break

        if msg1 == msg:
            acc += 1
        else:
            acc = 0;

        if acc == 100:
            break
        msg1 = msg
        print(acc, msg)



def main(client):
    myname = input('Type your name: ')


    try:
        s = threading.Thread(target=listen, args=(client, ), daemon=True)
        s.start()
    except:
        print('Some mistake...')

    while True:
        try:
            msg = input()
        except KeyboardInterrupt:
            msg = 'exit'

        res = "[ " + myname + " ]: " + msg


        try:
            client.send(res.encode('utf-8'))
        except:
            print('Error')

            break
        if msg == 'exit'.lower():
            break
    print('End main')


if __name__ == '__main__':
    main(client)





