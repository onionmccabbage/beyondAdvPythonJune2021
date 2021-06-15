import threading
import time

def standardThread():
    print('starting a standard thread')
    time.sleep(6)
    print('ending standard thread')

def daemonThread():
    while True:
        print('heartbeat...')
        time.sleep(1)

if __name__ == '__main__':
    s = threading.Thread(target=standardThread)
    d = threading.Thread(target=daemonThread)
    d.setDaemon(True)
    s.start()
    d.start()