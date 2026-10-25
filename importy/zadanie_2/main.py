from book import Book
from employee import Employee
from library import Library
from order import Order


# biblioteki
biblioteka_glowna = Library("Gliwice", "Łużycka", "44-040", "8-00:16-00", "809-098-123")
biblioteka_zachodnia = Library("Gliwice", "Sportowa", "44-040", "12-00:20-00", "809-098-123")

# 5 książek
book1 = Book(biblioteka_glowna, "automatyka dla początkujących", "15.06.2000", "Jan", "Nowak", 180)
book2 = Book(biblioteka_glowna, "C++", "15.08.1995", "Małgorzata", "Kowalska", 1000)
book3 = Book(biblioteka_zachodnia, "Graficzne tajniki gier", "20.06.2023", "Max", "Retz", 250)
book4 = Book(biblioteka_zachodnia, "Motywacja - jak pokonać niemożliwe", "20.05.2026", "Henryk", "Wielki", 199)
book5 = Book(biblioteka_zachodnia, "Matematyka dyskretna dla przeciętnych", "16.12.1999", "Witold", "Zadawski", 300)


# pracownicy
pracownik_blazej = Employee("Błażej", "Wielkomocny", "20.10.2023", "09.10.1980", "Gliwice", "Prosta", "44-040", "625-515-789")
pracownik_zygmunt = Employee("Zygmunt", "Widzistrzał", "09.01.2024", "08.08.2003", "Zabrze", "Potulna", "90-098", "621-756-794")
pracownik_monika = Employee("Monika", "Drzewiecka", "10.10.2026", "01.04.2000", "Gliwice", "Strzałkowa", "44-040", "986-232-123")

# studenci  Kuba, Hubert, Zosia
# ksiazki studentów
books_hubert = [book3, book5]
books_kuba = [book1, book4]
books_zosia = [book5, book3, book2]

# zamówienie
zamowienie_hubert = Order(pracownik_blazej, "Hubert", books_hubert, "20.10.2026")
zamowienie_kuba = Order(pracownik_zygmunt, "Kuba", books_kuba, "15.10.2026")
zamowienie_zosia = Order(pracownik_monika, "Zosia", books_zosia, "14.10.2026")


print(zamowienie_hubert)
print(zamowienie_kuba)
print(zamowienie_zosia)
