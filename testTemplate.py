from abc import ABCMeta, abstractmethod


# Example 1
class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()


class IOSCompiler(Compiler):

    def collectSource(self):
        print('Collecting Swift Source Code')

    def compileToObject(self):
        print('Compiling Swift code to LLVM bitcode')

    def run(self):
        print('Program running on runtime environment')


class Client:
    def main(self):
        self.ios = IOSCompiler()
        self.ios.compileAndRun()


# Example 2
class Trip(metaclass=ABCMeta):
    @abstractmethod
    def setTransport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def returnHome(self):
        pass

    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()


class VeniceTrip(Trip):

    def setTransport(self):
        print('Take a boat and find your way in the Grand Canal')

    def day1(self):
        print("Visit St Mark's Basilica")

    def day2(self):
        print("Doge's Palace")

    def day3(self):
        print('Enjoy the food')

    def returnHome(self):
        print('Get back')


class MaldivesTrip(Trip):
    def setTransport(self):
        print('On foot, on any island')

    def day1(self):
        print("Enjoy the marine life")

    def day2(self):
        print("Go for the water sports")

    def day3(self):
        print('Relax on the beach')

    def returnHome(self):
        print("Don't feel like leaving the beach")


class TravelAgency:
    def arrangeTrip(self):
        choice = input("What kind of place you'd like to go? [historical(h) or beach(b)] ")
        if choice == 'historical' or choice == 'h':
            self.trip = VeniceTrip()
        elif choice == 'beach' or choice == 'b':
            self.trip = MaldivesTrip()
        else:
            raise Exception('no such place')
        self.trip.itinerary()


if __name__ == '__main__':
    # client = Client()
    # client.main()

    ta = TravelAgency()
    ta.arrangeTrip()
