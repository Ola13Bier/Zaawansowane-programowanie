import base_data as bd


# obliczenie za pomocą pętli for
def CalculateFor():
    # wyczyszczenie listy answerList
    if (len(bd.answerList) > 1):
        bd.answerList.clear()
    # odwołanie do każdego elementu z listy
    for i in bd.numberList:
        # pomnozenie elementu przez 2
        x = i * 2
        # zapis do listy answerList
        bd.answerList.append(x)
    print("Zmiana zawartosci listy")


# obliczanie za pomocą listy składanej
def CalculateListComprehension():
    bd.answerList = []
    # obliczenie zawartości
    bd.answerList = [i * 2 for i in bd.numberList]
