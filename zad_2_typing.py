'''
Stworzyć funkcję, która przyjmie
2 argumenty typu int, a następnie 
zwróci wynik mnożenia obu liczb.
'''

#mnozenie liczb
def Multiplication(x: int, y: int):
    return (x * y)

x = 0

#pętla nieskończona
while(True):
    #wybór użytkownika czy chce uruchomić funkcję
    choice = input("Czy chcesz uruchomić funkcję?: 1:Tak 0:Nie, wyłącz program ")
    #instrukcja switch 
    match choice:
        #uruchom funkcję
        case "1":
            #pętla nieskończona
            while(True):
                #pobierz liczbę
                number_1=input("Podaj liczbę: ")
                #spróbuj
                try:
                    #czy to jest liczba
                    number_1 = int(number_1)
                    #przerwanie liczb
                    break
                #wyjatek
                except:
                    #komunikat
                    print("Niepoprawna watrość!!!")

            #petla nieskonczona
            while(True):
                #pobierz liczbę
                number_2=input("Podaj liczbę: ")
                #sprobuj
                try:
                    #czy to liczba
                    number_2 = int(number_2)
                    #przewij
                    break
                #wyjatek
                except:
                    #komunikat
                    print("Niepoprawna watrość!!!")
            #oblicz wynik mnożenia    
            mnoz = Multiplication(number_1,number_2)
            #wyświetl odpowiedź
            print(f"Mnozenie: {mnoz}")
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