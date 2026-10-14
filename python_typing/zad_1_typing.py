'''
Stworzyć funkcję, która przyjmuje 2 argumenty 
(typu string) name i surname, a następnie zwróci 
stringa zgodnie ze wzorem Cześć {name} {surname}! 
Należy uruchomić funkcję, wynik wykonania funkcji
 zapisać do zmiennej, a następnie go wyświetlić (print)
'''

#funkcja wyświetla tekst
def Hello(name: str, surname: str):
    #przypisanie zmiennej name do x_name
    x_name = name
    #przypisanie zmiennej surname do y_name
    y_surname = surname
    #wyswietlenie napisu
    print(f"Cześć {x_name} {y_surname}!")

x = 0
#pętla nieskończona
while(True):
    #wybór użytkownika czy chce uruchomić funkcję
    choice = input("Czy chcesz uruchomić funkcję?: 1:Tak 0:Nie, wyłącz program ")
    #instrukcja switch 
    match choice:
        #uruchom funkcję
        case "1":
            #pobierz od użytkokwnika imię
            name = input("Podaj imię: ")
            #pobierz od użytkownika nazwisko
            surname = input("Podaj nazwisko: ")
            #wykonaj funkcję
            Hello(name, surname)
        #nie uruhcamiaj
        case "0":
            #przerwij wykonywanie funckji
            x = 1
        #inna wartość komunikat
        case default:
            #wyswietl teskt
            print("Niepoprawna wartość")
    if x != 0:
        break