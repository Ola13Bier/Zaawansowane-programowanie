import os
import cv2


def Thershold_1(image, output_folder):
    # pobranie nazwy
    image = image[1]
    # pobierz nazwę zdjęcia
    image_name = os.path.basename(image)
    # pobranie obrazu
    img = cv2.imread(image)
    # konwersja zdjęcia w odcieniach szarości
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # odszumianie zdjęć metoda 1
    converted_img = cv2.threshold(cv2.GaussianBlur(gray_img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # ścieżka do zapisu
    output_path = os.path.join(
        # nazwa folderu
        output_folder,
        # nazwa pliku
        f"Odszumianie_threshold_{image_name}.png"
    )
    # czy plik istnieje
    if os.path.exists(output_path):
        # tak, wyświetl tekst
        print("plik istnieje")
    else:
        # nie, zapisz
        cv2.imwrite(output_path, converted_img)


def Thershold_2(image, output_folder):
    # pobranie nazwy
    image = image[1]
    # pobierz nazwę zdjęcia
    image_name = os.path.basename(image)
    # pobranie obrazu
    img = cv2.imread(image)
    # konwersja zdjęcia w odcieniach szarości
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # odszumianie zdjęć metoda 1
    converted_img = cv2.threshold(cv2.bilateralFilter(gray_img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # ścieżka do zapisu
    output_path = os.path.join(
        # nazwa folderu
        output_folder,
        # nazwa pliku
        f"Odszumianie_treshold_2_{image_name}.png"
    )
    # czy plik istnieje
    if os.path.exists(output_path):
        # tak, wyświetl tekst
        print("plik istnieje")
    else:
        # nie, zapisz
        cv2.imwrite(output_path, converted_img)


def Thershold_3(image, output_folder):
    # pobranie nazwy
    image = image[1]
    # pobierz nazwę zdjęcia
    image_name = os.path.basename(image)
    # pobranie obrazu
    img = cv2.imread(image)
    # konwersja zdjęcia w odcieniach szarości
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # odszumianie zdjęć metoda 1
    converted_img = cv2.threshold(cv2.medianBlur(gray_img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # ścieżka do zapisu
    output_path = os.path.join(
        # nazwa folderu
        output_folder,
        # nazwa pliku
        f"Odszumianie_treshold_3_{image_name}.png"
    )
    # czy plik istnieje
    if os.path.exists(output_path):
        # tak, wyświetl tekst
        print("plik istnieje")
    else:
        # nie, zapisz
        cv2.imwrite(output_path, converted_img)
