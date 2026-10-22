'''
Stworzyć funkcję, która przyjmuje 2 argumenty typu list
i zwraca wynik typu list. Funkcja ma za zadanie złączyć
przekazane listy w jedną, usunąć duplikaty, każdy element
podnieść do potęgi 3 stopnia, a następnie zwrócić
powstałą listę.
I założenie -> w listach może być wszystko liczby słowa
II założenie -> mogą mieć różne długości
'''

# lista definiowana przez użytkownika
lista_1 = []
lista_2 = []
lista_3 = []


# dodawanie wartosci dla obu list jest takie same
def Add(lista: list, y: int):
    # czyszczenie listy
    lista.clear()
    # petla for po elementach tablicy
    for i in range(0, y):
        # pobranie wartości
        value = input("Podaj parametr")
        # dodanie do listy
        lista.append(value)


def Connect():
    # lista globalna
    global lista_3
    # czyszczenie tablicy
    lista_3.clear()
    # dodanie listy 1 do listy 3
    lista_3.extend(lista_1)
    # dodanie listy 2 do listy 3
    lista_3.extend(lista_2)
    # usunięcie duplikatów w liscie 3
    lista_3 = set(lista_3)


# zatrzymanie
x = 0

# pętla nieskończona
while True:
    # wybór użytkownika czy chce uruchomić funkcję
    choice = input("Wybór: \n 0:Nie, wyłącz program \n 1: Dodaj do pierwszej listy \n2: Dodaj do drugiej listy \n3: Połączenie listy i wyświetlenie bez duplikatów")
    # instrukcja switch
    match choice:
        # Dodaj do listy
        case "1":
            # pętla nieskończona
            parametry = []
            while True:
                # pobierz liczbę
                number_1 = input("Podaj rozmiar: ")
                # spróbuj
                try:
                    # czy to jest liczba
                    number_1 = int(number_1)
                    # przerwanie liczb
                    break
                # wyjatek
                except ValueError:
                    # komunikat
                    print("Niepoprawna watrość!!!")
            # dodawanie do listy nowych parametrów
            Add(lista_1, number_1)
            # wyswietl
            print(f"Lista pierwsza: {lista_1}")
        case "2":
            while True:
                # pobierz liczbę
                number_1 = input("Podaj rozmiar: ")
                # spróbuj
                try:
                    # czy to jest liczba
                    number_1 = int(number_1)
                    # przerwanie liczb
                    break
                # wyjatek
                except ValueError:
                    # komunikat
                    print("Niepoprawna watrość!!!")
            # dodaj do listy 2
            Add(lista_2, number_1)
            # wyswietlanie odpowiedzi
            print(f"Lista druga: {lista_2}")
        # łączenie list
        case "3":
            # łączenie list i wyświetlenie bez duplikatów
            Connect()

            print(f"Lista trzecia: {lista_3}")
        # nie uruhcamiaj
        case "0":
            # przerwij wykonywanie funckji
            x = 1
        # inna wartość komunikat
        case default:
            # wyswietl teskt
            print("Niepoprawna wartość")

    # zatrzymanie pętli while(True)
    if x != 0:
        break
