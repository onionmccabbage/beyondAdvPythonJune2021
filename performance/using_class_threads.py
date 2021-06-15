from threading import Thread
class MyWorkerThread(Thread):
    def __init__(self):
        print('This is an instance of a thread')
        Thread.__init__(self)
    # we need a runable method
    def run(self):
        print('The thread is running')
if __name__ == '__main__':
    myThread = MyWorkerThread()
    myThread.start()
    myThread.join()