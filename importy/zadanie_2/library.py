# klasa opisująca bibliotekę
class Library:
    # dekralacja danych
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        # miasto
        self.city = city
        # ulica
        self.street = street
        # kod pocztowy
        self.zip_code = zip_code
        # godziny otwarcia
        self.open_hours = open_hours
        # numer telefonu
        self.phone = phone

    # wyświetlenie danych
    def __str__(self):
        return (
            f"miasto: {self.city} \n"
            f"ulica: {self.street} \n"
            f"kod pocztowy: {self.zip_code} \n"
            f"godziny otwarcia: {self.open_hours} \n"
            f"telefon: {self.phone} \n"
            f"{'*' * 20}"
        )
