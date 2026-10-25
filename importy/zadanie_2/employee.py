# klasa opisująca pracownika biblioteki
class Employee:
    # deklaracja zmiennych
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        # imie
        self.first_name = first_name
        # nazwisko
        self.last_name = last_name
        # data zatrudnienia
        self.hire_date = hire_date
        # data urodzenia
        self.birth_date = birth_date
        # miasto
        self.city = city
        # ulica
        self.street = street
        # kod pocztowy
        self.zip_code = zip_code
        # numer telefonu
        self.phone = phone

    # wyświetlenie danych
    def __str__(self):
        return (
            f"imię: {self.first_name} \n"
            f"nazwisko: {self.last_name} \n"
            f"data zatrudnienia: {self.hire_date} \n"
            f"data urodzenia: {self.birth_date} \n"
            f"miasto: {self.city} \n"
            f"ulica: {self.street} \n"
            f"kod pocztowy: {self.zip_code} \n"
            f"numer telefonu: {self.phone}"
            f"{'*' * 20}"
        )
