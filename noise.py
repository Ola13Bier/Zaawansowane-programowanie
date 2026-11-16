import os
import cv2
import list_images as li
import noise_median_blur
import noise_threshold_1
import noise_adaptive


# odczytaj tekst z listy zdjęć
def Read_list_images():
    # znajdź zdjęcia
    lista = li.List_img()
    # folder do zapisu wyniki
    output_folder = "odszumione"
    # utworzenie folderu, jeśli nie istnieje
    os.makedirs(output_folder, exist_ok=True)
    # pętla for po elementach zdjęcia
    for image in enumerate(lista):
        # odszummianie median blur
        noise_median_blur.Median_blur(image, output_folder)
        noise_threshold_1.Thershold_1(image, output_folder)
        noise_threshold_1.Thershold_2(image, output_folder)
        noise_threshold_1.Thershold_3(image, output_folder)
        noise_adaptive.Adaptive_thershold_1(image,output_folder)
        noise_adaptive.Adaptive_thershold_2(image,output_folder)
        noise_adaptive.Adaptive_thershold_3(image,output_folder)

Read_list_images()
