import base_data as bd


# wyswietl aktualna liste
def Show():
    # wyswietlenie napisu
    print("Aktualna lista")
    # petla for po numberList
    for i in bd.numberList:
        # wyświetlenie wartości
        print(i)


# pokazanie
def ShowAnswer():
    # wyswietlenie napisu
    print("Lista wyników")
    # petla for po elementach answerList
    for i in bd.answerList:
        # wyświetlenie wartosci
        print(i)
