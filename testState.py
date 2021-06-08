from abc import ABCMeta, abstractmethod


# Example 1
class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    def handle(self):
        print('ConcreteStateA')


class ConcreteStateB(State):
    def handle(self):
        print('ConcreteStateB')


class Context:
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def handle(self):
        self.state.handle()


# Example 2
class TVState(metaclass=ABCMeta):
    @abstractmethod
    def doThis(self):
        pass


class StartState(TVState):
    def doThis(self):
        print('TV Switching ON..')


class StopState(TVState):
    def doThis(self):
        print('TV Switching OFF..')


class TVContext:
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def doThis(self):
        self.state.doThis()


# Example 3
class ComputerState:
    name = 'state'
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print(f'Current: {self} => switched to new state {state.name}')
            self.__class__ = state
        else:
            print(f'Current: {self} => switching to {state.name} not possible')

    def __str__(self):
        return self.name


class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']


class Off(ComputerState):
    name = 'off'
    allowed = ['on']


class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']


class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


class Computer:
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def getState(self):
        print(f'Current state: {self.state}')
        return self.state

    def change(self, state):
        self.state.switch(state)


if __name__ == '__main__':
    # ctx = Context()
    # stateA = ConcreteStateA()
    # stateB = ConcreteStateB()
    # ctx.setState(stateB)
    # ctx.handle()
    # ctx.setState(stateA)
    # ctx.handle()

    # ctx = TVContext()
    # print(ctx.getState())
    # start = StartState()
    # stop = StopState()
    # ctx.setState(stop)
    # ctx.doThis()

    comp = Computer()
    comp.getState()
    comp.change(On)
    comp.change(Off)
    comp.change(On)
    comp.change(Suspend)
    comp.change(Hibernate)
    comp.change(On)
    comp.change(Off)
    comp.getState()
