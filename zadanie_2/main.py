'''
Endpoint pod adresem `/movies`, który zwraca
listę filmów w postaci obiektów json.
Kroki do wykonania:
- pobrać dane z pliku
- stworzyć klasę Movie
(posłuży jako model danych)
- przeiterować pętlą po wierszach
z pliku i stworzyć tyle obiektów
klasy Movie ile wierszy
- wykorzystać metodę magiczną`__dict__` do serializacji obiektu
- zwrócić z metody listę
zserializowanych obiektów
'''
import os
from fastapi import FastAPI
import csv
from zadanie_2_movie import Movie

# API
app = FastAPI()


# strona główna
@app.get("/")
# funkcja dla strony głównej
def home():
    # wyświetlenie tekstu
    return {"hello": "world"}


# strona wyświetlająca dane o filmach
@app.get("/movies")
# funkcja wyświetlająca dane o filmach
def Movies():
    # deklaracja listy filmów
    listMovies = []

    # ścieżka do katalogu wraz z nazwą
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # ścieżka do pliku movies.csv
    file_path = os.path.join(BASE_DIR, "movies.csv")

    # otwarcie pliku za pomocą ścieżki w kodie UTF-8
    # przeznaczonym tylko do odczytu jako plik
    with open(file_path, "r", encoding="utf-8") as file:
        # odczytanie pliku o rozszerzeniu csv i tworzenie słownika
        # poprzez pominięcie przecinków między słowami
        reader = csv.DictReader(file, delimiter=",")

        # pętla po odczytanych elementach
        for row in reader:
            # zapis danych z obiektów do zmiennej movie
            # utworzonej z klasy Movie
            movie = Movie(
                row["movieId"],
                row["title"],
                row["genres"]
            )
            # dodanie zmiennej do listy filmów
            listMovies.append(movie.__dict__)
    # wyświetlenie zawartości listy
    return listMovies
