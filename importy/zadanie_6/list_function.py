from base_data import *


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
