import threading
import time
import random

def threadWorker():
    print('the thread is running')
    time.sleep(2)
    print('the thread is terminating')

def executeThread(i):
    print('Thread {} has started'.format(i))
    sleepTime = random.randint(1,4)
    time.sleep(sleepTime)
    print('Thread {} has finished executing'.format(i))

if __name__ == '__main__':
    myThread = threading.Thread(target=threadWorker)
    myThread.start()
    myThread.join() # optional, but a good idea

    for i in range(10):
        thread = threading.Thread(target=executeThread, args=(i,)) # arguments as a tuple
        thread.start()
        print('Active Threads: ', threading.enumerate())
        thread.join()