import sqlite3


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        return f'<Person ({self.name}, {self.age})>'


class Adder:
    def __init__(self):
        self.sum = 0

    def add(self, value):
        self.sum += value


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            # print(cls)
            cls.__instance = super().__new__(cls)
        return cls.__instance


class LazySingleton:
    __instance = None

    def __init__(self):
        if not LazySingleton.__instance:
            print('__init__ method called..')
        else:
            print('Instance already created:', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance


# class Borg:
#     __shared_state = {'1': '2'}
#
#     def __init__(self):
#         self.x = 11
#         self.__dict__ = self.__shared_state

class Borg:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class MyInt(type):
    def __new__(mcs, *args, **kwargs):
        print('create new class:', mcs, args, kwargs)
        # cls = type.__new__(mcs, *args, *kwargs)
        cls = super().__new__(mcs, *args, *kwargs)
        return cls

    def __init__(cls, *args, **kwargs):
        print('init new class:', cls, args, kwargs)
        # type.__init__(cls, *args, **kwargs)
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('Here is my int:', args)
        # return type.__call__(cls, *args, **kwargs)
        return super().__call__(*args, **kwargs)


class Int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MetaSingleton(type):
    __instances = {}

    # def __new__(mcs, *args, **kwargs):
    #     print('create new class:', mcs, args, kwargs)
    #     # cls = type.__new__(mcs, *args, *kwargs)
    #     cls = super().__new__(mcs, *args, *kwargs)
    #     return cls
    #
    # def __init__(cls, *args, **kwargs):
    #     print('init new class:', cls, args, kwargs)
    #     # type.__init__(cls, *args, **kwargs)
    #     super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            print('create cursor object')
            self.connection = sqlite3.connect('sqlitedb/test2')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


class Database1:
    _instance = None
    connection = None

    def __new__(cls, *args, **kwargs):
        if Database1._instance is None:
            Database1._instance = super().__new__(cls, *args, **kwargs)
        return Database1._instance

    def connect(self):
        if self.connection is None:
            print('create cursor object')
            self.connection = sqlite3.connect('sqlitedb/test2')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if HealthCheck._instance is None:
            HealthCheck._instance = super().__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append('Server 1')
        self._servers.append('Server 2')
        self._servers.append('Server 3')
        self._servers.append('Server 4')

    def changeServer(self):
        self._servers.pop()
        self._servers.append('Server 5')


if __name__ == '__main__':
    print(f'\n-------------------------- {__debug__ = } --------------------------\n')

    # p = Person('John', 32)
    # print('Type of Object:', type(p), 'Memory Address:', id(p))

    # acc = Adder()
    # for i in range(99):
    #     acc.add(i)
    # print(acc.sum, 99 * 98 / 2)

    # s = Singleton()
    # s1 = Singleton()
    # print(s, s1)

    # s = LazySingleton()
    # print('Object created:', s.getInstance())
    # s1 = LazySingleton()
    # print(LazySingleton.getInstance())

    # b = Borg()
    # b1 = Borg()
    # print(b, b1)
    # print(b.__dict__, b1.__dict__)
    # b.x = 4
    # print(b.__dict__, b1.__dict__)

    # i = Int(4, 6)

    # l1 = Logger()
    # l2 = Logger()
    # print(l1, l2)

    # db1 = Database().connect()
    # db2 = Database().connect()
    # print(db1, db2)

    db1 = Database1().connect()
    db2 = Database1().connect()
    print(db1, db2)

    # hc1 = HealthCheck()
    # hc2 = HealthCheck()
    # hc1.addServer()
    # print(hc1._servers)
    # hc2.changeServer()
    # print(hc2._servers)
