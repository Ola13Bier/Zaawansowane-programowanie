import base_data as bd


# Wyswietlanie co drugiego elementu
def ShowOnlyTwoNumber():
    # lista zawierająca co drugi element
    twoNumber = []
    # petla od 1 i inkrementajcą co 2
    for i in range(1, len(bd.numbers), 2):
        # dodanie elementu do listy twoNumber
        twoNumber.append(bd.numbers[i])
    # Wyswietlenie listy
    print("Liczba parzysta: ", twoNumber)
