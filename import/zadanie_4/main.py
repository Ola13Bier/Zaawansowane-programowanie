import base_data as bd
import list_function as lf
import show_data as sh


# Wyboru dla użytkownika
print("1 - Dodaj elementy do listy \n2 - Dodaj losowe liczby do listy \n3 - Wyswietl co drugi element")
# pętla nieskończona
while True:
    # pobrana wartość od użytkownika
    choice = input("Wybor:")
    # switch
    match choice:
        case "1":
            # Dodaj do listy
            lf.AddNumbersToList()
            # wyswietlenie listy
            print(bd.numbers)
        case "2":
            # dodaj losowe liczby
            # poczatek
            x = input("Zakres poczatkowy:")
            # koniec
            y = input("Zakres koncowy:")
            # sprobuj wykonać
            try:
                # konwert x na int
                x = int(x)
                # konwert y na int
                y = int(y)
                # zalozenie ze x jest mniejsze niz y
                if (x < y):
                    # funkcja gdy x < y
                    lf.AddRandomNumbersToList(x, y)
                else:
                    # funkcja gdy y < x
                    lf.AddRandomNumbersToList(y, x)
            # wyjatek
            except ValueError:
                # komunikat
                print("Niepoprawne parametry")
        case "3":
            # Pokaz liczby parzyste
            sh.ShowOnlyTwoNumber()
        case _:
            # Scenariusz alternatywny
            print("Niepoprawna wartość")
