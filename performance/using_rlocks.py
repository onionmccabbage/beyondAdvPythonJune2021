# rlock is re-entrant lock
import threading
import time

class MyWorker():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock() # re-entrant lock
    def modifyA(self):
        with self.rlock: # 'with' will automatically call 'join()' when done
            print('RLock acquired {} modifying A'. format(self.rlock._is_owned() ))
            print(self.rlock) # examine the re-entrant lock
            self.a += 1
            time.sleep(1)
    def modifyB(self):
        with self.rlock: # 'with' will automatically call 'join()' when done
            print('RLock acquired {} modifying B'. format(self.rlock._is_owned() ))
            print(self.rlock) # examine the re-entrant lock
            self.b -= 1
            time.sleep(1) 
    def modifyBoth(self):
        with self.rlock: # 'with' will automatically call 'join()' when done
            print('RLock acquired {} modifying A and B'. format(self.rlock._is_owned() ))
            print(self.rlock) # examine the re-entrant lock
            self.modifyA()
            self.modifyB()
            time.sleep(1)
        print(self.rlock)       

def main():
    worker = MyWorker()
    worker.modifyB()
    worker.modifyBoth()
    worker.modifyA()



if __name__ == '__main__':
    main()