# Wartość wyrazu 1
a0 = 0
# Wartość wyrazu 2
a1 = 1


# funkcja obliczająca wartości dla ciągu Fibonacciego
def Fibonnaci(n: int):
    # wartość n mniejsza niż 0
    if n < 0:
        # Błąd, brak obliczeń
        return None

    # n jest równa 0
    if n == 0:
        # zwróć pierwszy element
        return a0

    # n równe 1
    if n == 1:
        # zwróć wartość drugiego elementu
        return a1
    else:
        # rekurencja, obliczanie wartości
        return Fibonnaci(n - 1) + Fibonnaci(n - 2)
