from property import Property


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
