#Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie wyświetli każde z nich. 
'''
założenie do zadania

lista na mieć 5 elementów
'''

#deklaracja listy
name_list = []

#funkcja dodawania 
def AddToList():
    #sprawdzenie czy długość listy jest równa 5
    if len(name_list) == 5:
            print("Brak miejsca")
    else:
        #użytkownik podaje imię
        name = input("Podaj imie: ")
        #wartość jest dodawana do listy
        name_list.append(name)
    
#funkcja czyszcząca listę
def ClearList():
    #lista pusta
    name_list.clear()

#wyświetlenie zawartości listy
def PrintList(x):
    #pętla odnosząca się od wartości listy/tablicy 
    for i in x:
        #wyświetlenie zawartości
        print(i)

#wyświetlenie pięciu elementów z listy
def PrintFiveName(x):
        #sprawdzenie długości
        if len(x) == 5: 
            #wyświetlenie elementów poprzez ich pozycję
            print(x[0], x[1], x[2], x[3], x[4])
        else:
            #Długość jest mniejsze niż 5 elementów
            #wyznaczanie brakujących elementów
            y = 5 - len(x)
            #wyswietlenie liczby brakujących elementów
            print("Brakuje ",y)
#Wyboru dla użytkownika
print("1 - Dodaj imie do listy  2 - Wyczysc liste  3 - Wyswietl zawartosc listy 4 - wyswietl całą listę \n")
#pętla nieskończona
while (True):
    #pobrana wartość od użytkownika
    choice = input("podaj liczbe:")
    #switch
    match choice:
        case "1":
            #Dodaj do listy
            AddToList()
        case "2":
            #wyczyść listę
            ClearList()
        case "3":
            #wyświetl zawartość
            PrintList(name_list)
        case "4":
            #wyświetl całą listę
            PrintFiveName(name_list)
        case _:
            #Scenariusz alternatywny
            print("Niepoprawna wartość")

