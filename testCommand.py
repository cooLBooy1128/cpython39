import time
from abc import ABCMeta, abstractmethod


# Example 1
class Wizard:
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def excute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print('Copying binaries --', self.src, 'to', self.rootdir)
            else:
                print('No Operation')


# Example 2
class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        self.recv.action()


class Receiver:
    def action(self):
        print('Receiver action')


class Invoker:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


# Example 3
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class StockTrade:
    @staticmethod
    def buy():
        print('You will buy stocks')

    @staticmethod
    def sell():
        print('You will sell stocks')


class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        print(f'Agent:: place {type(order).__name__}')

    def execute(self):
        for order in self.__orderQueue:
            order.execute()


if __name__ == '__main__':
    # wizard = Wizard('python3.9.gzip', r'D:\ProgramFiles')
    # # Users chooses to install Python only
    # wizard.preferences({'python': True})
    # wizard.preferences({'java': False})
    # wizard.excute()

    # recv = Receiver()
    # cmd = ConcreteCommand(recv)
    # invoker = Invoker()
    # invoker.command(cmd)
    # invoker.execute()

    # client
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)
    # invoker
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
    print('--', time.ctime(), '--')
    time.sleep(2)
    print('--', time.ctime(), '--')
    agent.execute()
