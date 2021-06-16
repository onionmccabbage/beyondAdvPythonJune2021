import multiprocessing

def myProcFn():
    print('Executing child process (with its own copy of Python and no GIL limits)')

def main():
    print('Executing the main process')
    myProc2 = multiprocessing.Process(target=myProcFn)
    myProc3 = multiprocessing.Process(target=myProcFn)
    myProc4 = multiprocessing.Process(target=myProcFn)
    myProc5 = multiprocessing.Process(target=myProcFn)
    myProc6 = multiprocessing.Process(target=myProcFn)

    myProc2.start()
    myProc3.start()
    myProc4.start()
    myProc5.start()
    myProc6.start()

    myProc2.join()
    myProc3.join()
    myProc4.join()
    myProc5.join()
    myProc6.join()

if __name__ == '__main__':
    main()