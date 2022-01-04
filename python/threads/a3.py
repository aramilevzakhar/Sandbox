from concurrent.futures import ThreadPoolExecutor
import logging
import threading
import time



def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    #with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #    executor.map(thread_function, range(10))
    threads = []


    arr = ['rwrew', 'fadf', 'ewrwrewrer', 123, '324']
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, arr, timeout=2)

    


        



    """
    for i in range(10):
        x = threading.Thread(target=thread_function, args=(i,), daemon=True)
        threads.append(x)
        x.start()
    for i, thread in enumerate(threads):
        thread.join()
        #print(i)
    """
