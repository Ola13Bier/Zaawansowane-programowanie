import os
import cv2


def Median_blur(image, output_folder):
    # pobranie nazwy
    image = image[1]
    # pobierz nazwę zdjęcia
    image_name = os.path.basename(image)
    # pobranie obrazu
    img = cv2.imread(image)
    # odszumianie zdjęć metoda 1
    converted_img = cv2.medianBlur(img, 3)
    # ścieżka do zapisu
    output_path = os.path.join(
        # nazwa folderu
        output_folder,
        # nazwa pliku
        f"Odszumianie_median_Blur_{image_name}.png"
    )
    # czy plik istnieje
    if os.path.exists(output_path):
        # tak, wyświetl tekst
        print("plik istnieje")
    else:
        # nie, zapisz
        cv2.imwrite(output_path, converted_img)
