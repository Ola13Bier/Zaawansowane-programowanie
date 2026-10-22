'''
1. Stworzyć następujące klasy:
    - Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
        - area
        - rooms (int)
        - price
        - address
    - House (klasa dziedzicząca klasę `Property`, która opisuje dom), posiadająca pola:
        - plot (rozmiar działki, int)
    - Flat (klasa dziedzicząca klasę `Property`, która opisuje mieszkanie), posiadająca pola:
        - floor

    Dodatkowo:

    - Każda z klas dziedziczących ma mieć zaimplementowaną metodę `__str__` , która będzie opisywała obiekt.
    - Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem konstruktora.
    - Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić.
'''


# klasa opisująca posiadłość/ nieruchomość
class Property():
    # konstruktor
    def __init__(self, area, rooms: int, price, address):
        # powierzchnia
        self.area = area
        # liczba pokoi
        self.rooms = rooms
        # cena nieruchomoś
        self.price = price
        # adres
        self.address = address

    # wyswietlenie danych
    def __str__(self):
        return (
            f"powierzchnia: {self.area}\n"
            f"liczba pokoi: {self.rooms}\n"
            f"cena: {self.price}\n"
            f"adres: {self.address}\n"
        )


# klasa dziedzicząca klasę Property. opisuje dom
class House(Property):
    # konstruktor
    def __init__(self, area, rooms, price, address, plot: int):
        # dane z klasy dziedziczonej
        super().__init__(area, rooms, price, address)
        # rozmiar działki
        self.plot = plot

    # wyświetl
    def __str__(self):
        return (
            super().__str__() + f"rozmiar działki: {self.plot}"
        )


# klasa dziedzicząca klasę `Property`, która opisuje mieszkanie
class Flat(Property):
    # konstruktor
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        # pietro mieszkania
        self.floor = floor

    # wyświetlenie
    def __str__(self):
        return (
            super().__str__() + f"pietro: {self.floor}"
        )


# deklaracja obiektu klasy House
dom = House("180", "4", "800000", "74-400 Dębno, ul Nizinna 5", 43)
# wyświetlenie informacji
print("Dane o domie")
print(dom)

# deklaracja obiektu klasy flat
mieszkanie = Flat("50", 2, "540000", "74-400 Dębno, ul Jana Pawła 19/6", 4)
# wyświetlenie informacji.
print("Dane o mieszkaniu")
print(mieszkanie)
