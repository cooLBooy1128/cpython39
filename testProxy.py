from abc import ABCMeta, abstractmethod


# example 1
class Actor:
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print(f'{type(self).__name__} is occupied with current movie')

    def avaliable(self):
        self.isBusy = False
        print(f'{type(self).__name__} is free for the movie')

    def getStatus(self):
        return self.isBusy


class Proxy:
    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.avaliable()


# example 2
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print(f'Bank:: Checking if Account {self.__getAccount()} has enough funds')
        return True
        # return False

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print('Bank:: Paying the merchant')
            return True
        else:
            print('Bank:: Sorry, not enough funds!')
            return False


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input('Proxy:: Punch in Card Number: ')
        self.bank.setCard(card)
        return self.bank.do_pay()


class You:
    def __init__(self):
        print('You:: Lets buy the Denim shirt')
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print('You:: Denim shirt is Mine :-)')
        else:
            print('You:: I should earn more :(')


if __name__ == '__main__':
    print('-' * 50 + '\n')

    # r = Proxy()
    # r.work()

    you = You()
    you.make_payment()
