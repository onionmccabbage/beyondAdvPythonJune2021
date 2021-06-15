import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self, barrier):
        threading.Thread.__init__(self) # we must call the __init__ of the parent super-class
        self.__barrier = barrier
    def run(self):
        print('Thread {} is busy ...'.format(threading.current_thread() ))
        time.sleep(random.randint(1,3))
        print('thread {} is joining but must wait on a barrier ({} waiting)'.format(threading.current_thread(), self.__barrier))
        self.__barrier.wait() # wait until the barrier is lifted (in this case, 4)
        print('Barrier lifted, carry on ...')

def main():
    barrier = threading.Barrier(4) # limit of 4
    threads = []
    for i in range(8): # this will be 'batched' 4 at a time
        thread = MyThread(barrier)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()