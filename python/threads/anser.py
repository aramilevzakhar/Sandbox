from threading import Thread

import time

def funcPrintA():
    for _ in range(10):
        print("a", end=" ")
        time.sleep(0.001)

def funcPrintB():
    for _ in range(10):
        print("b", end=" ")
        time.sleep(0.001)


if __name__ == '__main__':
    thread1 = Thread(target=funcPrintA).start()
    thread2 = Thread(target=funcPrintB).start()

print("hello world")    


