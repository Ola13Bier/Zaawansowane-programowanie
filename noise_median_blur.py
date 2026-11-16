import os
import cv2


def Median_blur(image, output_folder):
    # pobranie nazwy
    image = image[1]
    # pobierz nazwę zdjęcia
    image_name = os.path.basename(image)
    # pobranie obrazu
    img =cv2.imread(image)
    # odszumianie zdjęć metoda 1
    converted_img = cv2.medianBlur(img, 3)
    # ścieżka do zapisu
    output_path = os.path.join(
        output_folder,
        f"Odszumianie_median_Blur_{image_name}.png"
    )

    if os.path.exists(output_path):
        print("plik istnieje")
    else:
        cv2.imwrite(output_path, converted_img)