'''
Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range), a następnie
wyświetli co drugi element

Założenie:
- lista deklarowana przez uzytkownika
- losowo wybrane wartości z zakresu wybranego przez uzytkownika
'''
#biblioteka random
import random

#lista globalna
numbers = []

#dodanie 10 elemtów do listy
def AddNumbersToList():
    numbers.clear()
    #petla od 0 do 9
    for i in range(10):
        #petla nieskonczona
        while (True):
            #pobranie wartosci
            x = input("Podaj wartosc: ")
            #sprobuj wykonać
            try:
                #skonwertuj na float
                x = float(x)
                #dodaj do listy
                numbers.append(x)
                #przerwij petle
                break
            #wyjatek
            except:
                #komunikat
                print("Niepoprawna wartosc")
    #lista jest pelna
    print("Lista pelna")

def AddRandomNumbersToList(x, y):
    #sprobuj wykonać
    try:
        #czy zmienna x jest typu int
        x = int(x)
        #czy zmienna y jest typu int
        y = int(y)
        #wyczysc liste
        numbers.clear()
        #petla od 0 do 9
        for i in range(10):
            #losowanie liczby z zakresu
            a = random.randint(x, y)
            #dodanie wartości
            numbers.append(a)
    #wyjatek
    except:
        #komunikat
        print("Parametr nie jest liczba")
    print("Lista: ", numbers)

#Wyswietlanie co drugiego elementu
def ShowOnlyTwoNumber():
    #lista zawierająca co drugi element 
    twoNumber = []
    #petla od 1 i inkrementajcą co 2
    for i in range(1 , len(numbers), 2):
        #dodanie elementu do listy twoNumber
        twoNumber.append(numbers[i])
    #Wyswietlenie listy
    print("Liczba parzysta: ", twoNumber)

#Wyboru dla użytkownika
print("1 - Dodaj elementy do listy  \n2 - Dodaj losowe liczby do listy \n3 - Wyswietl co drugi element")
#pętla nieskończona
while (True):
    #pobrana wartość od użytkownika
    choice = input("Wybor:")
    #switch
    match choice:
        case "1":
            #Dodaj do listy
            AddNumbersToList()
            #wyswietlenie listy
            print(numbers)
        case "2":
            #dodaj losowe liczby
            #poczatek
            x = input("Zakres poczatkowy:")
            #koniec
            y = input("Zakres koncowy:")
            #sprobuj wykonać
            try:
                #konwert x na int
                x = int(x)
                #konwert y na int
                y = int(y)
                #zalozenie ze x jest mniejsze niz y
                if (x < y):
                    #funkcja gdy x < y
                    AddRandomNumbersToList(x,y)
                else:
                    #funkcja gdy y < x
                    AddRandomNumbersToList(y,x)
            #wyjatek
            except:
                #komunikat
                print("Niepoprawne parametry")
        case "3":
            #Pokaz liczby parzyste
            ShowOnlyTwoNumber()
        case _:
            #Scenariusz alternatywny
            print("Niepoprawna wartość")
