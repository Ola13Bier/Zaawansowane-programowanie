from property import Property


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
