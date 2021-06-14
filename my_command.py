from abc import ABCMeta, abstractmethod

# an abstract class
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class StockTrade:
    def buy(self):
        print('buy stocks')
    def sell(self):
        print('sell stocks')

class Agent:
    def __init__(self):
        self.__orderQueue = [] # here we use an empty list
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

# concrete classes derived from abstract 'Order' class
class BuyStock(Order):
    def __init__(self, stock):
        self.stock = stock
    def execute(self):
        return self.stock.buy()

class SellStock(Order):
    def __init__(self, stock):
        self.stock = stock
    def execute(self):
        return self.stock.sell()

if __name__ == '__main__':
    # client
    stock = StockTrade()
    buy = BuyStock(stock)
    sell = SellStock(stock)
    # invoker
    agent = Agent()
    agent.placeOrder(buy)
    agent.placeOrder(sell)

    