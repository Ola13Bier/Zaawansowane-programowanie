from show import *


x = 0
# pętla nieskończona
while True:
    # wybór użytkownika czy chce uruchomić funkcję
    choice = input("Czy chcesz uruchomić funkcję?: 1:Tak 0:Nie, wyłącz program ")
    # instrukcja switch
    match choice:
        # uruchom funkcję
        case "1":
            # pobierz od użytkokwnika imię
            name = input("Podaj imię: ")
            # pobierz od użytkownika nazwisko
            surname = input("Podaj nazwisko: ")
            # wykonaj funkcję
            Hello(name, surname)
        # nie uruhcamiaj
        case "0":
            # przerwij wykonywanie funckji
            x = 1
        # inna wartość komunikat
        case default:
            # w yswietl teskt
            print("Niepoprawna wartość")
    if x != 0:
        break
