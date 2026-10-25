# deklaracja listy
name_list = []


# funkcja dodawania
def AddToList():
    # sprawdzenie czy długość listy jest równa 5
    if len(name_list) == 5:
        print("Brak miejsca")
    else:
        # użytkownik podaje imię
        name = input("Podaj imie: ")
        # wartość jest dodawana do listy
        name_list.append(name)


# funkcja czyszcząca listę
def ClearList():
    # lista pusta
    name_list.clear()
