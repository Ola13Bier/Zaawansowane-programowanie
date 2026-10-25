from list_function import *


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
