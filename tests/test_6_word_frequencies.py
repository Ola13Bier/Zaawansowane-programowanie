# import biblioteki string
import string


# funkcja zwraca słownik z częstością występowania słów w tekście
def word_frequencies(text: str) -> dict:
    # zmiana dużych liter na małe
    text = text.lower()

    # pętla for po interpunkcyjnych
    for znak in string.punctuation:
        # zamienia znak
        text = text.replace(znak, "")

    # rozdzielenie tekstu na słowa
    words = text.split()

    # pusty słownik
    frequencies = {}

    # pętla po słowach
    for word in words:
        # jeśli wyraz zawiera się w słowniku zwiększa ich liczbę
        if word in frequencies:
            # wzrost liczby słów
            frequencies[word] += 1
        else:
            # dodanie nowego słowa
            frequencies[word] = 1

    # zwróć słownik
    return frequencies
