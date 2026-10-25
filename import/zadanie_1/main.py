import display_function as df
import list_function as lf


# Wyboru dla użytkownika
print("1 - Dodaj imie do listy  2 - Wyczysc liste  3 - Wyswietl zawartosc listy 4 - wyswietl całą listę \n")
# pętla nieskończona
while True:
    # pobrana wartość od użytkownika
    choice = input("podaj liczbe:")
    # switch
    match choice:
        case "1":
            # Dodaj do listy
            lf.AddToList()
        case "2":
            # wyczyść listę
            lf.ClearList()
        case "3":
            # wyświetl zawartość
            df.PrintList(lf.name_list)
        case "4":
            # wyświetl całą listę
            df.PrintFiveName(lf.name_list)
        case _:
            # Scenariusz alternatywny
            print("Niepoprawna wartość")
