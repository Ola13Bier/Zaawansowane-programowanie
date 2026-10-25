# lista podanych liczb
numberList = []
# lista odpowiedzi
answerList = []


def AddNumberList():
    # pętla nieskończona, zatrzymuje się gdy liczba elementów wynosi 5
    while (len(numberList) != 5):
        # pobranie wartości od użytkownika
        number = input("Podaj liczbe: ")
        try:
            # czy można skonwertować zmienną na wartość
            number = float(number)
            # można zmienić na typ liczbowy
            numberList.append(float(number))
        except ValueError:
            # wartosc number jest liczbowa
            print("Niepoprawna wartosc")
    # wyswietlanie napisu
    print("Lista zawiera 5 elemntów")


def Clear():
    numberList.clear()
