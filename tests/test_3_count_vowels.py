# funckja zlicza liczbę samogłosek w danym ciągu
def Count_vowels(text: str) -> int:
    # zmienna zawierająca wszystkie samogłoski
    vowels = "AaĄąEeĘęYyUuIiOoÓó"
    # zmienna zliczająca samogłoski
    count = 0
    # pętla for po elementach tekstu
    for i in range(0, len(text)):
        # czy znak zawiera się w zmiennej vowels
        if text[i] in vowels:
            # zwieksz wartość count o 1
            count += 1
    # zwróć liczbę policzonych samogłosek
    return count
