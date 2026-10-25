import base_data as bd
import random


# dodanie 10 elemtów do listy
def AddNumbersToList():
    for i in range(10):
        while True:
            x = input("Podaj wartosc: ")
            try:
                x = float(x)
                bd.numbers.append(x)
                break
            except ValueError:
                print("Niepoprawna wartosc")
    print("Lista pelna")


def AddRandomNumbersToList(x, y):
    try:
        x = int(x)
        y = int(y)

        bd.numbers.clear()
        for i in range(10):
            a = random.randint(x, y)
            bd.numbers.append(a)
    except ValueError:
        print("Parametr nie jest liczba")
