import random
from abc import ABC, ABCMeta, abstractmethod

class Payment(metaclass = ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    def __getAccount(self):
        self.account = self.card # use a debit card
        return self.account
    def __hasFunds(self):
        print('Bank is checking if account {} has sufficent funds'.format(self.__getAccount()))
        return bool(random.getrandbits(1)) # a fast way to return True or False
    def setCard(self, card):
        self.card = card
    def do_pay(self):
        if self.__hasFunds():
            print('Bank is paying the merchant')
            return True
        else:
            print('Bank says not enough money')
            return False

class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
    def do_pay(self):
        card = input('Payment Proxy: Swipe card or Tap phone? ')
        self.bank.setCard(card)
        return self.bank.do_pay()

class You: # client
    def __init__(self):
        print('I want a cup of coffee')
        self.debitCard = DebitCard()
        self.isPurchased = None
    def makePayment(self):
        self.isPurchased = self.debitCard.do_pay()
    def __del__(self):
        if self.isPurchased:
            print('yummie')
        else:
            print('anyone lend me a fiver?')

if __name__ == '__main__':
    you = You()
    you.makePayment()