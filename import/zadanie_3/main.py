import list_function as lf
import show_data as sd
import base_data as bd


# Wyboru dla użytkownika
print("1 - Dodaj elementy do listy  \n2 - Dodaj losowe liczby do listy \n3 - Pokaz liczby parzyste")
# pętla nieskończona
while (True):
    # pobrana wartość od użytkownika
    choice = input("Wybor:")
    # switch
    match choice:
        case "1":
            # Dodaj do listy
            lf.AddNumbersToList()
            print(bd.numbers)
        case "2":
            # dodaj losowe liczby
            x = input("Zakres poczatkowy:")
            y = input("Zakres koncowy:")
            try:
                x = int(x)
                y = int(y)
                if (x < y):
                    lf.AddRandomNumbersToList(x, y)
                else:
                    lf.AddRandomNumbersToList(y, x)
            except ValueError:
                print("Niepoprawne parametry")
            print(bd.numbers)
        case "3":
            # Pokaz liczby parzyste
            sd.ShowOnlyEvenNumber()
        case _:
            # sScenariusz alternatywny
            print("Niepoprawna wartość")
