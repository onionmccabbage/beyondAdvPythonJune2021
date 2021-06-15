import threading
import time
import random

class TicketSeller(threading.Thread):
    ticketsSold = 0
    def __init__(self, semaphore):
        threading.Thread.__init__(self)
        self.__semaphore = semaphore
        print('Ticket seller starts selling tickets')
    def run(self):
        global ticketsAvailable
        running = True
        while running: # auto release when done
            self.randomDelay()
            self.__semaphore.acquire()
            if ticketsAvailable <=0:
                running = False
            else:
                self.ticketsSold += 1
                ticketsAvailable -= 1
                print('{} sold {} so there are {} remaining'.format(self.getName(), self.ticketsSold, ticketsAvailable) )
            self.__semaphore.release() # ... so other sellers can use it!
        print('Ticket seller {} sold {} tickets in total'.format(self.getName(), self.ticketsSold))
    def randomDelay(self):
        time.sleep(random.randint(0, 4)/4) # 0, 0.25, 0.5 or 0.75 sec

def main():
    semaphore = threading.Semaphore(value=4) # up to 4 at a time
    sellers = [] # a list of ticket sellers
    for i in range(4):
        seller = TicketSeller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()

if __name__ == '__main__':
    ticketsAvailable = 200 # a global variable
    main()
