'''
Utwórz funkcję, która otrzyma w parametrze listę
zawierającą 5 dowolnych liczb, każdy jej element
pomnoży przez 2, a na końcu ją zwróci.
'''

#lista podanych liczb
numberList = []
#lista odpowiedzi
answerList = []

def AddNumberList():
    #pętla nieskończona, zatrzymuje się gdy liczba elementów wynosi 5
    while (len(numberList) != 5):
        #pobranie wartości od użytkownika
        number = input("Podaj liczbe: ")
        try:
        #czy można skonwertować zmienną na wartość
            number = float(number)
            #można zmienić na typ liczbowy
            numberList.append(float(number))
        except:
            #wartosc number jest liczbowa
            print("Niepoprawna wartosc")
    #wyswietlanie napisu
    print("Lista zawiera 5 elemntów")

def Clear():
    numberList.clear()

#wyswietl aktualna liste        
def Show():
    #wyswietlenie napisu
    print("Aktualna lista")
    #petla for po numberList
    for i in numberList:
        #wyświetlenie wartości
        print(i)

#obliczenie za pomocą pętli for
def CalculateFor():
    #wyczyszczenie listy answerList
    if (len(answerList) > 1):
        answerList.clear()
    #odwołanie do każdego elementu z listy
    for i in numberList:
        #pomnozenie elementu przez 2
        x = i * 2
        #zapis do listy answerList
        answerList.append(x)
    print("Zmiana zawartosci listy")


#obliczanie za pomocą listy składanej
def CalculateListComprehension():
    answerList = []
    #obliczenie zawartości
    answerList = [i * 2 for i in numberList]
   


#pokazanie
def ShowAnswer():
    #wyswietlenie napisu
    print("Lista wyników")
    #petla for po elementach answerList
    for i in answerList:
        #wyświetlenie wartosci
        print(i)


#Wyboru dla użytkownika
print("1 - Dodaj elementy do listy  2 - Pokaz liste liczb  3 - Obliczenia za pomoca for  4 - obliczanie za pomocą listy skladanej 5 - wyswietl wynik\n")
#pętla nieskończona
while (True):
    #pobrana wartość od użytkownika
    choice = input("Wybor:")
    #switch
    match choice:
        case "1":
            #Dodaj do listy
            AddNumberList()
        case "2":
            #pokaz liste liczb
            Show()
        case "3":
            #obliczenie za pomocą pętli for
            CalculateFor()
        case "4":
            #Obliczanie za pomaca listy skladanej
            CalculateListComprehension()
        case "5":
            print(answerList)
        case _:
            #Scenariusz alternatywny
            print("Niepoprawna wartość")