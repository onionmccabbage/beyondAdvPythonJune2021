import multiprocessing
import os

class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()
    def run(self):
        print( 'Child process ID is {}'.format(multiprocessing.current_process().pid ) )

def main():
    print('Executing the main process')
    myProcess = MyProcess()
    myProcess.start()
    myProcess.join()
    # a bunch of child process
    processes = []
    for i in range(os.cpu_count()):
        proc = MyProcess()
        processes.append(proc)
        proc.start()
    for proc in processes:
        proc.join()

if __name__ == '__main__':
    main()