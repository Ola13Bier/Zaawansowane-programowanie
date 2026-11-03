# sprawdza, czy liczba jest pierwsza
def Is_prime(n: int) -> bool:
    # najmniejsza liczba pierwsza to 2, więc nie może być mniejsza niż 2
    if n < 2:
        # zwróć fałsz
        return False
    # pętla od 2 do n
    for i in range(2, n):
        # czy liczba jest podzielna przez inne liczby
        if n % i == 0:
            # zwróć fałsz
            return False
    # zwróć True
    return True
