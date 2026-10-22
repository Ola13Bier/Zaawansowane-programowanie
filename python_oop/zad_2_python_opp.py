''''
Stworzyć następujące klasy:
Library (klasa opisująca bibliotekę), posiadająca pola:
- city
- street
- zip_code
- open_hours (str)
- phone
Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
    - first_name
    - last_name
    - hire_date
    - birth_date
    - city
    - street
    - zip_code
    - phone
Book (klasa opisująca książkę), posiadająca pola
    - library
    - publication_date
    - author_name
    - author_surname
    - number_of_pages
Order (klasa opisująca zamówienie), posiadająca pola:
    - employee
    - student
    - books (lista obiektów klasy Book)
    - order_date
Dodatkowo:

- Każda klasa ma mieć zaimplementowaną metodę `__str__`, 
która będzie opisywała obiekt oraz ewentualne obiekty 
znajdujące się w tym obiekcie (np. obiekt Library w 
obiekcie Book).
- Pola w klasie mają być zdefiniowane jako atrybuty 
ustawiane podczas tworzenia instancji klasy za 
pośrednictwem konstruktora.
- Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 
3 pracowników, 3 studentów, oraz 2 zamówienia.
- Wyświetlić oba zamówienia (`print`)
'''
#klasa opisująca bibliotekę
class Library:
    #dekralacja danych
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        #miasto
        self.city = city
        #ulica
        self.street = street
        #kod pocztowy
        self.zip_code= zip_code
        #godziny otwarcia
        self.open_hours  = open_hours 
        #numer telefonu
        self.phone = phone

    #wyświetlenie danych
    def __str__(self):
        return (
            f"miasto: {self.city} \n" 
            f"ulica: {self.street} \n" 
            f"kod pocztowy: {self.zip_code} \n" 
            f"godziny otwarcia: {self.open_hours} \n" 
            f"telefon: {self.phone} \n" 
             f"{'*' * 20}"
        )

#klasa opisująca pracownika biblioteki
class Employee:
    #deklaracja zmiennych
    def __init__(self,first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        #imie
        self.first_name = first_name
        #nazwisko
        self.last_name = last_name
        #data zatrudnienia
        self.hire_date = hire_date
        #data urodzenia
        self.birth_date = birth_date
        #miasto
        self.city = city
        #ulica
        self.street = street
        #kod pocztowy
        self.zip_code = zip_code
        #numer telefonu
        self.phone = phone

    #wyświetlenie danych
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

#klasa opisująca książkę
class Book:
    #deklaracji zmiennych
    def __init__(self, library, title, publication_date, author_name, author_surname, number_of_page):
        #nazwa biblioteki
        self.library = library
        #tytuł książki
        self.title = title
        #data publikacji
        self.publication_date = publication_date
        #imię autora
        self.author_name = author_name
        #nazwisko autora
        self.author_surname = author_surname
        #liczba stron
        self.number_of_pages = number_of_page
    #wyswietlanie 
    def __str__(self):
        return (
            f"nazwa biblioteki: {self.library} \n"
            f"tytuł: {self.title} \n"
            f"data publikacji: {self.publication_date} \n"
            f"imię autora: {self.author_name} \n" 
            f"nazwisko autora: {self.author_surname} \n" 
            f"liczba stron: {self.number_of_pages} \n"
             f"{'*' * 20}\n"
        )
    def __repr__(self):
        return self.__str__()
             
#klasa opisująca zamówienie
class Order:
    #deklaracja danych
    def __init__(self,employee, student, books, order_date ):
        #pracownik
        self.employee = employee
        #student
        self.student = student
        #ksiazki
        self.books = books
        #data zamówienia
        self.order_date = order_date

    #wyświetlenie danych
    def __str__(self):
        lista_ksiazek = "\n".join(str(book) for book in self.books)
        return (
            f"pracownik: {self.employee} \n"
            f"student: {self.student} \n"
            f"ksiazki: {lista_ksiazek} \n"
            f"data zamówienia: {self.order_date} \n"
        )

#biblioteki
biblioteka_glowna = Library("Gliwice", "Łużycka", "44-040", "8-00:16-00", "809-098-123")
biblioteka_zachodnia = Library("Gliwice", "Sportowa", "44-040", "12-00:20-00", "809-098-123")

# 5 książek
book1 = Book(biblioteka_glowna, "automatyka dla początkujących","15.06.2000" ,"Jan", "Nowak",180)
book2 = Book(biblioteka_glowna, "C++","15.08.1995" ,"Małgorzata", "Kowalska",1000)
book3 = Book(biblioteka_zachodnia, "Graficzne tajniki gier", "20.06.2023","Max", "Retz",250)
book4 = Book(biblioteka_zachodnia, "Motywacja - jak pokonać niemożliwe", "20.05.2026","Henryk", "Wielki",199)
book5 = Book(biblioteka_zachodnia, "Matematyka dyskretna dla przeciętnych","16.12.1999" ,"Witold", "Zadawski",300)


#pracownicy
pracownik_blazej = Employee("Błażej", "Wielkomocny", "20.10.2023", "09.10.1980", "Gliwice", "Prosta", "44-040", "625-515-789")
pracownik_zygmunt = Employee("Zygmunt", "Widzistrzał", "09.01.2024", "08.08.2003", "Zabrze", "Potulna", "90-098", "621-756-794")
pracownik_monika = Employee("Monika", "Drzewiecka", "10.10.2026", "01.04.2000", "Gliwice", "Strzałkowa", "44-040", "986-232-123")

#studenci  Kuba, Hubert, Zosia
#ksiazki studentów
books_hubert = [book3, book5]
books_kuba = [book1, book4]
books_zosia = [book5, book3, book2]

#zamówienie
zamowienie_hubert = Order(pracownik_blazej,"Hubert", books_hubert, "20.10.2026")
zamowienie_kuba = Order(pracownik_zygmunt,"Kuba", books_kuba, "15.10.2026")
zamowienie_zosia = Order(pracownik_monika,"Zosia", books_zosia, "14.10.2026")


print(zamowienie_hubert)
print(zamowienie_kuba)
print(zamowienie_zosia)