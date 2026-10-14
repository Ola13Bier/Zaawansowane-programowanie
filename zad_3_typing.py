'''
Stworzyć funkcję, która będzie sprawdzała
czy przekazana liczba w parametrze jest 
parzysta i zwróci tą informację jako
typ logiczny bool (True/False). Należy 
uruchomić funkcję, wynik wykonania 
zapisać do zmiennej, a następnie 
wykorzystując warunek logiczny 
wyświetlić prawidłowy tekst 
"Liczba parzysta" / "Liczba nieparzysta"
'''

def Parzysta(number: int):
    if number % 2 == 0:
        return True
    else:
        return False

x = 0

#pętla nieskończona
while(True):
    #wybór użytkownika czy chce uruchomić funkcję
    choice = input("Czy chcesz uruchomić funkcję?: 1:Tak 0:Nie, wyłącz program ")
    #instrukcja switch 
    match choice:
        #uruchom funkcję
        case "1":
            #pętla nieskończona dla pobrania właściwego parametru
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
            value = Parzysta(number_1)


            #if value == True: "parzysta" / "nieparzysta"
            if value == True:
                print("Liczba parzysta")
            else:
                print("Liczba nieparzysta")
            
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