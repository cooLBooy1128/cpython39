import functools
import sys
import time
import tkinter
from warnings import warn


class MyStack(list):
    def push(self, item):
        self.append(item)

    def pop(self):
        return super(MyStack, self).pop()


class MyQueue(list):
    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return super(MyQueue, self).pop(0)


class MyIterator:
    def __init__(self, iterable=None):
        if iterable is None:
            self.data = []
        else:
            self.data = list(iterable)
        self.idx = -1

    def __next__(self):
        if self.idx >= len(self.data) - 1:
            raise StopIteration
        self.idx += 1
        return self.data[self.idx]

    def __iter__(self):
        return self


class Counter:
    def __init__(self, start=0):
        self.start = start

    def __call__(self):
        self.start += 1
        return self.start


class InstTrack:
    count = 0  # count is class attr

    def __init__(self):  # increment count
        InstTrack.count += 1

    def __del__(self):  # decrement count
        InstTrack.count -= 1

    @staticmethod
    def how_many():  # return count
        return InstTrack.count

    @classmethod
    def test_class_method(cls):
        print('this is a class method')


class NonZero(int):
    def __init__(self, arg):
        print('init NonZero')

    def __new__(cls, arg):
        print(f"new {cls}: {arg}")
        return super().__new__(cls, arg) if arg != 0 else None


class UpperStr(str):
    def __new__(cls, val):
        return super(UpperStr, cls).__new__(cls,
                                            val.upper())


class WrapMe:
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return repr(self.__data)

    def __getattr__(self, name):
        print(f'get attr: {name}')
        return getattr(self.__data, name)


class TestSlots:
    __slots__ = ('a', 'b', 'c')
    d = 10


class SetDescr:
    def __set__(self, instance, value):
        pass


class DataDescr:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        value = getattr(instance, self.private_name)
        print(f'Accessing {self.public_name!r} giving {value!r}')
        return value

    def __set__(self, instance, value):
        print(f'Updating {self.public_name!r} to {value!r}')
        setattr(instance, self.private_name, value)


class UseDescr:
    set_descr = SetDescr()
    data_descr = DataDescr()


class HideX:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return ~self.__x

    @x.setter
    def x(self, x):
        assert isinstance(x, int), f'{x!r} must be an integer!'
        self.__x = ~x


class MetaC(type):
    def __init__(cls, name, bases, attrd):
        super().__init__(name, bases, attrd)
        print('*** Created class %r at: %s' % (
            name, time.ctime()))


class Foo(metaclass=MetaC):
    def __init__(self):
        print('*** Instantiated class %r at: %s' % (
            self.__class__.__name__, time.ctime()))


class ReqStrSugRepr(type):
    def __init__(cls, name, bases, attrd):
        super().__init__(
            name, bases, attrd)
        if '__str__' not in attrd:
            raise TypeError(
                'Class requires overriding of __str__()')
        if '__repr__' not in attrd:
            warn(
                'Class suggests overriding of __repr__()\n',
                stacklevel=3)


class Foo1(metaclass=ReqStrSugRepr):
    def __str__(self):
        return 'Instance of class:', self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


# class Foo2(metaclass=ReqStrSugRepr):
#     def __str__(self):
#         return 'Instance of class:', self.__class__.__name__


# class Foo3(metaclass=ReqStrSugRepr):
#     pass


def time_deco(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        res = f(*args, **kwargs)
        t = time.perf_counter() - t0
        print(f'{f} elapsed time: {t}')
        return res

    return wrapper


@time_deco
def test1(x, y):
    res = []
    for i in range(x):
        for j in range(y):
            res.append(i + j)
    return res


def pfa():
    root = tkinter.Tk()
    MyButton = functools.partial(tkinter.Button, root, fg='white', bg='blue')
    b1 = MyButton(text='Button 1')
    b2 = MyButton(text='Button 2')
    qb = MyButton(text='QUIT', bg='red', command=root.quit)
    b1.pack()
    b2.pack()
    qb.pack(fill=tkinter.X, expand=True)
    root.title('PFAs!')
    root.mainloop()


def foo(x=0):
    print('\ncalling foo()...')
    aString = 'bar'
    anInt = 42
    print("foo()'s globals:", globals())
    print("foo()'s locals:", locals())


if __name__ == '__main__':
    print(sys.argv, __debug__)
    print(sys.path)
    # print(list(sys.modules.keys()))
    # print(test1.__name__, test1)
    # print(test1(140, 130))
    # pfa()
    # foo()
    # print(globals() is locals())

    # xx = WrapMe(1 + 2j)
    # print(xx.get())
    # print(xx.real)
    # print(xx.conjugate())
