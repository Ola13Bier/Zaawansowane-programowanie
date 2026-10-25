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
