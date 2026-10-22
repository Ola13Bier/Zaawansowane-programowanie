'''
Stworzyć funkcję, która przyjmie 3 argumenty typu int
i sprawdzi czy suma dwóch pierwszych liczb jest większa
lub równa trzeciej, a następnie zwróci tę informację
jako typ logiczny bool
'''


# funkcja zwraca typ bool
def Oblicz(x: int, y: int, z: int):
    # sprawdzenie czy x + y jest większe niż z
    if (x + y) >= z:
        # prawda
        return True
    else:
        # fałsz
        return False


x = 0


# pętla nieskończona
while True:
    # wybór użytkownika czy chce uruchomić funkcję
    choice = input("Czy chcesz uruchomić funkcję?: 1:Tak 0:Nie, wyłącz program ")
    # instrukcja switch
    match choice:
        # uruchom funkcję
        case "1":
            # pętla nieskończona
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

            # petla nieskonczona
            while True:
                # pobierz liczbę
                number_2 = input("Podaj liczbę: ")
                # sprobuj
                try:
                    # czy to liczba
                    number_2 = int(number_2)
                    # przewij
                    break
                # wyjatek
                except ValueError:
                    # komunikat
                    print("Niepoprawna watrość!!!")
            while True:
                # pobierz liczbę
                number_3 = input("Podaj liczbę: ")
                # sprobuj
                try:
                    # czy to liczba
                    number_3 = int(number_3)
                    # przewij
                    break
                # wyjatek
                except ValueError:
                    # komunikat
                    print("Niepoprawna watrość!!!")

            # obliczanie wyników
            answer = Oblicz(number_1, number_2, number_3)
            print(f"Wartość logincz wyniku: {answer}")

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
