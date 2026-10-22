'''
Stworzyć funkcję, która przyjmie 2 argumenty.
Pierwszy typu list, a drugi typu int .
Funkcja ma sprawdzić (zwracając typ logiczny bool),
czy lista z parametru pierwszego zawiera taką wartość
jaką przekazano w parametrze drugim.
'''
# lista parametrow
parametry = []


# czy lista zawiera wartość parametru
def CzyListaZawieraParametr(tab: list, i: int):
    # ile razy występuje dany paramert w liscie
    ans = tab.count(i)
    # wystepowanie jest rowne 0
    if ans == 0:
        # nie zawiera
        return False
    # występuje chociaż raz
    else:
        # zawiera
        return True


# dodaj parametry do listy ile chcesz
def DodajDoListy(x: int):
    # pętla do ilosci podanej przez użytkownka
    for i in range(0, x):
        # Pobierz parametr
        y = input(f"Podaj {i + 1} liczbe: ")
        # Czy dane są liczba
        try:
            # próba konwertacji na typ całkowity
            y = int(y)
            # dodanie parametru
            parametry.append(y)
        # typ nie jest całkowity
        except ValueError:
            # komunikat
            print("To nie jest liczba!!!")


# zatrzymanie
x = 0


# pętla nieskończona
while True:
    # wybór użytkownika czy chce uruchomić funkcję
    choice = input("Wybór: \n 0:Nie, wyłącz program \n 1: Dodaj do listy 2: czy lista zawierz parametr ")
    # instrukcja switch
    match choice:
        # Dodaj do listy
        case "1":
            # pętla nieskończona
            parametry = []
            while True:
                # pobierz liczbę
                number_1 = input("Podaj rozmiar: ")
                # spróbuj
                try:
                    # czy to jest liczba
                    number_1 = int(number_1)
                    # przerwanie liczb
                    break
                # wyjatek
                except ValueError:
                    # komunikat
                    print("Niepoprawna watrość!!!")
            # dodawanie do listy nowych parametrów
            DodajDoListy(number_1)
        case "2":
            while True:
                # pobierz liczbę
                number_1 = input("Podaj liczbę: ")
                # spróbuj
                try:
                    # czy to jest liczba
                    number_1 = int(number_1)
                    # przerwanie liczb
                    break
                # wyjatek
                except ValueError:
                    # komunikat
                    print("Niepoprawna watrość!!!")
            # odpowiedz czy lista zawiera dany element
            ans = CzyListaZawieraParametr(parametry, number_1)
            # wyswietlanie odpowiedzi
            print(f"Czy lista zawiera element {number_1}? {ans}")
        # nie uruhcamiaj
        case "0":
            # przerwij wykonywanie funckji
            x = 1
        # inna wartość komunikat
        case default:
            # wyswietl teskt
            print("Niepoprawna wartość")
    if x != 0:
        break
