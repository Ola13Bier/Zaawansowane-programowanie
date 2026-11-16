# z biblioteki pathlib importuj Path
from pathlib import Path


# wybrany folder images
folder = Path("images")
# globalna lista zdjęć
list_i = []


# funkcja zapisująca tylko pliki zdjęciowe
def List_img():
    # rozszerzenia plików
    exends = [".jpeg", ".jpg", ".png", ".bmp"]

    # odwołanie globalne do zmiennej
    global list_i
    # zapisywanie lokalizacji i nazw do listy
    list_i = [
        plik for plik in folder.iterdir()
        # jeśli jest to plik i zawiera rozszerzenie z listy  to zapisz
        if plik.is_file() and plik.suffix.lower() in exends
    ]
    # zwróć listę
    return list_i
