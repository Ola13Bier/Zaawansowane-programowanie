'''
Utwórz funkcję, która otrzyma w parametrze listę 
10 liczb (rekomendowane wykorzystanie funkcji range),
a następnie wyświetli jedynie parzyste elementy.

Założenie:
- lista deklarowana przez uzytkownika
- losowo wybrane wartości z zakresu wybranego przez uzytkownika
'''
import random

#lista globalna
numbers = []

#dodanie 10 elemtów do listy
def AddNumbersToList():
    for i in range(10):
        while (True):
            x = input("Podaj wartosc: ")
            try:
                x = float(x)
                numbers.append(x)
                break
            except:
                print("Niepoprawna wartosc")
    print("Lista pelna")

def AddRandomNumbersToList(x, y):
    try:
        x = int(x)
        y = int(y)

        numbers.clear()
        for i in range(10):
            a = random.randint(x, y)
            numbers.append(a)
    except:
        print("Parametr nie jest liczba")

def ShowOnlyEvenNumber():
    evenNumber = []
    for i in numbers:
        if i % 2 == 0 :
            evenNumber.append(i)
    evenNumber.sort()
    print("Liczba parzysta: ", evenNumber)

#Wyboru dla użytkownika
print("1 - Dodaj elementy do listy  \n2 - Dodaj losowe liczby do listy \n3 - Pokaz liczby parzyste")
#pętla nieskończona
while (True):
    #pobrana wartość od użytkownika
    choice = input("Wybor:")
    #switch
    match choice:
        case "1":
            #Dodaj do listy
            AddNumbersToList()
            print(numbers)
        case "2":
            #dodaj losowe liczby
            x = input("Zakres poczatkowy:")
            y = input("Zakres koncowy:")
            try:
                x = int(x)
                y = int(y)
                if (x < y):
                    AddRandomNumbersToList(x,y)
                else:
                    AddRandomNumbersToList(y,x)
            except:
                print("Niepoprawne parametry")
            print(numbers)
        case "3":
            #Pokaz liczby parzyste
            ShowOnlyEvenNumber()
        case _:
            #Scenariusz alternatywny
            print("Niepoprawna wartość")
