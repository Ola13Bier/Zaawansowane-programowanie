import os
import cv2


def Adaptive_thershold_1(image, output_folder):
    # pobranie nazwy
    image = image[1]
    # pobierz nazwę zdjęcia
    image_name = os.path.basename(image)
    # pobranie obrazu
    img = cv2.imread(image)
    # konwersja zdjęcia w odcieniach szarości
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # odszumianie zdjęć metoda 1
    converted_img = cv2.adaptiveThreshold(cv2.GaussianBlur(gray_img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # ścieżka do zapisu
    output_path = os.path.join(
        output_folder,
        f"Odszumianie_adaptive_threshold_{image_name}.png"
    )
    if os.path.exists(output_path):
        print("plik istnieje")
    else:
        cv2.imwrite(output_path, converted_img)


def Adaptive_thershold_2(image, output_folder):
    # pobranie nazwy
    image = image[1]
    # pobierz nazwę zdjęcia
    image_name = os.path.basename(image)
    # pobranie obrazu
    img = cv2.imread(image)
    # konwersja zdjęcia w odcieniach szarości
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # odszumianie zdjęć metoda 1
    converted_img = cv2.adaptiveThreshold(cv2.bilateralFilter(gray_img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # ścieżka do zapisu
    output_path = os.path.join(
        output_folder,
        f"Odszumianie_adaptive_treshold_2_{image_name}.png"
    )
    if os.path.exists(output_path):
        print("plik istnieje")
    else:
        cv2.imwrite(output_path, converted_img)


def Adaptive_thershold_3(image, output_folder):
    # pobranie nazwy
    image = image[1]
    # pobierz nazwę zdjęcia
    image_name = os.path.basename(image)
    # pobranie obrazu
    img = cv2.imread(image)
    # konwersja zdjęcia w odcieniach szarości
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # odszumianie zdjęć metoda 1
    converted_img = cv2.adaptiveThreshold(cv2.medianBlur(gray_img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # ścieżka do zapisu
    output_path = os.path.join(
        # nazwa folderu
        output_folder,
        # nazwa pliku
        f"Odszumianie_adaptive_treshold_3_{image_name}.png"
    )
    # czy plik istnieje
    if os.path.exists(output_path):
        # tak, wyświetl tekst
        print("plik istnieje")
    else:
        # nie, zapisz
        cv2.imwrite(output_path, converted_img)
