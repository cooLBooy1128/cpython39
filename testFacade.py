class EventAssistant:
    def __init__(self):
        print('Event Assistant:: Let me talk to the folks\n')

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()
        self.florist = Florist()
        self.florist.setFlowerRequirements()
        self.caterer = Caterer()
        self.caterer.setCuisine()
        self.musician = Musician()
        self.musician.setMusicType()


class Hotelier:
    def __init__(self):
        print('Arranging the Hotel for Marriage --')

    def _isAvaliable(self):
        print('Is the Hotel free for the event on given day?')
        return True

    def bookHotel(self):
        if self._isAvaliable():
            print('Registered the Booking\n\n')


class Florist:
    def __init__(self):
        print('Flower Decorations for the Event --')

    def setFlowerRequirements(self):
        print('Carnations, Roses and Lilies would be used for Decorations\n\n')


class Caterer:
    def __init__(self):
        print('Food Arrangements for the Event --')

    def setCuisine(self):
        print('Chinese & Continental Cuisine to be served\n\n')


class Musician:
    def __init__(self):
        print('Musical Arrangements for the Event --')

    def setMusicType(self):
        print('Jazz and Classical will be played\n\n')


class You:
    def __init__(self):
        print('You:: Whoa! Marriage Arrangements??!!!')

    def askEventAssistant(self):
        print("You:: Let's Contact the Event Assistant\n\n")
        es = EventAssistant()
        es.arrange()

    def __del__(self):
        print('You:: Thanks to Event Assistant, all preparations done! Phew!')


if __name__ == '__main__':
    print('\n' + '-' * 50 + '\n')

    you = You()
    you.askEventAssistant()
