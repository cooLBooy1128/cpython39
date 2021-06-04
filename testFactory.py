from abc import ABCMeta, abstractmethod


# 简单工厂方法
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print('Woof Woof!!')


class Cat(Animal):
    def do_say(self):
        print('Meow Meow!!')


class ForestFactory:
    @staticmethod
    def make_sound(object_type):
        return eval(object_type)().do_say()


# 工厂方法模式
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print('Personal Section')


class PatentSection(Section):
    def describe(self):
        print('Patent Section')


class AlbumSection(Section):
    def describe(self):
        print('Album Section')


class PublicationSection(Section):
    def describe(self):
        print('Publication Section')


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class Linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class Facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


# 抽象工厂模式
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, vegpizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print(f'Prepare {type(self).__name__}')


class ChickenPizza(NonVegPizza):
    def serve(self, vegpizza):
        print(f'{type(self).__name__} is served with Chicken on {type(vegpizza).__name__}')


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print(f'Prepare {type(self).__name__}')


class HamPizza(NonVegPizza):
    def serve(self, vegpizza):
        print(f'{type(self).__name__} is served with Ham on {type(vegpizza).__name__}')


class PizzaStore:
    def orderPizza(self):
        country = input('which country pizza do you want to order? [Indian or US] ')
        self.factory = eval(country + 'PizzaFactory')()
        kind = input('which kind of pizza do you want to order? [Veg or NonVeg] ')
        self.vegpizza = self.factory.createVegPizza()
        if kind == 'Veg':
            self.vegpizza.prepare()
        elif kind == 'NonVeg':
            self.nonvegpizza = self.factory.createNonVegPizza()
            self.nonvegpizza.serve(self.vegpizza)
        else:
            raise Exception(f"{kind} pizza didn't exist")

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.nonvegpizza = self.factory.createNonVegPizza()
            self.vegpizza = self.factory.createVegPizza()
            self.vegpizza.prepare()
            self.nonvegpizza.serve(self.vegpizza)


if __name__ == '__main__':
    print('\n' + '-' * 50 + '\n')
    # ff = ForestFactory()
    # animal = input('Which animal should make sound? [Dog or Cat] ')
    # ff.make_sound(animal.capitalize())

    # profile_type = input("Which Profile you'd like to create? [Linkedin or Facebook] ")
    # profile = eval(profile_type.capitalize())()
    # print('Creating Profile..', type(profile).__name__)
    # print('Profile has sections --', profile.getSections())

    pizza = PizzaStore()
    pizza.makePizzas()
    pizza.orderPizza()
