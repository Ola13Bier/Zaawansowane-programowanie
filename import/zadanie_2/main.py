import calculate as cal
import show_data as sd
import base_data as bd


# Wyboru dla użytkownika
print("1 - Dodaj elementy do listy  2 - Pokaz liste liczb  3 - Obliczenia za pomoca for  4 - obliczanie za pomocą listy skladanej 5 - wyswietl wynik\n")
# pętla nieskończona
while (True):
    # pobrana wartość od użytkownika
    choice = input("Wybor:")
    # switch
    match choice:
        case "1":
            # Dodaj do listy
            bd.AddNumberList()
        case "2":
            # pokaz liste liczb
            sd.Show()
        case "3":
            # bliczenie za pomocą pętli for
            cal.CalculateFor()
        case "4":
            # Obliczanie za pomaca listy skladanej
            cal.CalculateListComprehension()
        case "5":
            print(bd.answerList)
        case _:
            # Scenariusz alternatywny
            print("Niepoprawna wartość")
