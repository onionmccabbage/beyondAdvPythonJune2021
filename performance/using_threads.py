import threading

def whoAmI(what):
    print("Thread {} says {}".format(threading.current_thread(), what))

if __name__ == '__main__':
    whoAmI('I am the main program')
    for n in range(4):
        p = threading.Thread(target=whoAmI, args=('I am a function on a thread'))
        p.start()