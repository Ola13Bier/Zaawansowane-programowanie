from base_data import *


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
