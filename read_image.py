import pytesseract
from PIL import Image
import cv2
import numpy as np
import list_images as li

# ścieżka do tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# odczytywanie tekstu ze zdjęć
def read_text(img):
    # znajdź tekst na zdjęciu, język polski
    tekst = pytesseract.image_to_string(
        img,
        lang="pol"
    )
    # wyświetl tekst
    print(tekst)


# odczytaj tekst z listy zdjęć
def read_list_images():
    # znajdź zdjęcia
    lista = li.List_img()
    # pętla for po zdjęciach
    for img in lista:
        # otwórz zdjęcie
        image = Image.open(img)
        image = np.array(image)
        # konwertuj na czarno-białe
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # wyświetl lokalizacje i nazwe zdjęcia
        print(f"\n--- Zdjęcie: {img} ---")
        # przeczytaj tekst ze zdjęcia
        read_text(image)


# uruchomienie czytania z listy
read_list_images()
