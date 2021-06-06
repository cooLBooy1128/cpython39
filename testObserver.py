from abc import ABCMeta, abstractmethod


# Example 1 - push model
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f'{type(self).__name__} :: Got {args} From {subject}')


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f'{type(self).__name__} :: Got {args} From {subject}')


# Example 2 - pull model (maybe)
class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return 'Got News:', self.__latestNews


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Observer):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber(Observer):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    # subject = Subject()
    # observer1 = Observer1(subject)
    # observer2 = Observer2(subject)
    # subject.notifyAll('notification')

    news_publishers = NewsPublisher()
    for Sub in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Sub(news_publishers)
    print('Subscribers:', news_publishers.subscribers())
    news_publishers.notifySubscribers()
    print()
    news_publishers.addNews('Hello World!')
    news_publishers.notifySubscribers()
    print('\nDetached:', type(news_publishers.detach()).__name__)
    print('Subscribers:', news_publishers.subscribers())
    news_publishers.addNews('My second news!')
    news_publishers.notifySubscribers()
