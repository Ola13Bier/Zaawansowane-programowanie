# wyświetlenie zawartości listy
def PrintList(x):
    # pętla odnosząca się od wartości listy/tablicy
    for i in x:
        # wyświetlenie zawartości
        print(i)


# wyświetlenie pięciu elementów z listy
def PrintFiveName(x):
    # sprawdzenie długości
    if len(x) == 5:
        # wyświetlenie elementów poprzez ich pozycję
        print(x[0], x[1], x[2], x[3], x[4])
    else:
        # Długość jest mniejsze niż 5 elementów
        # wyznaczanie brakujących elementów
        y = 5 - len(x)
        # wyswietlenie liczby brakujących elementów
        print("Brakuje ", y)
