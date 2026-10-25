import random
import base_data as bd


# dodanie 10 elemtów do listy
def AddNumbersToList():
    bd.numbers.clear()
    # petla od 0 do 9
    for i in range(10):
        # petla nieskonczona
        while (True):
            # pobranie wartosci
            x = input("Podaj wartosc: ")
            # sprobuj wykonać
            try:
                # skonwertuj na float
                x = float(x)
                # dodaj do listy
                bd.numbers.append(x)
                # przerwij petle
                break
            # wyjatek
            except ValueError:
                # komunikat
                print("Niepoprawna wartosc")
    # lista jest pelna
    print("Lista pelna")


def AddRandomNumbersToList(x, y):
    # sprobuj wykonać
    try:
        # czy zmienna x jest typu int
        x = int(x)
        # czy zmienna y jest typu int
        y = int(y)
        # wyczysc liste
        bd.numbers.clear()
        # petla od 0 do 9
        for i in range(10):
            # losowanie liczby z zakresu
            a = random.randint(x, y)
            # dodanie wartości
            bd.numbers.append(a)
    # wyjatek
    except ValueError:
        # komunikat
        print("Parametr nie jest liczba")
    print("Lista: ", bd.numbers)
