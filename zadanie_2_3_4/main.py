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

Dodać nowe modele wraz z endpointem wyświetlającym zawartość
'''
import os
from fastapi import FastAPI
import csv
from zadanie_2_movie import Movie
from zadanie_3a_link import Link
from zadanie_3b_rating import Rating
from zadanie_3c_tag import Tag

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


# strona wyświetlająca linki
@app.get("/links")
# funkcja wyświetlająca linki
def Links():
    # deklaracja listy linków
    listLinks = []

    # ścieżka do katalogu wraz z nazwą
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # ścieżka do pliku links.csv
    file_path = os.path.join(BASE_DIR, "links.csv")

    # otwarcie pliku za pomocą ścieżki w kodie UTF-8
    # przeznaczonym tylko do odczytu jako plik
    with open(file_path, "r", encoding="utf-8") as file:
        # odczytanie pliku o rozszerzeniu csv i tworzenie słownika
        # poprzez pominięcie przecinków między słowami
        reader = csv.DictReader(file, delimiter=",")

        # pętla po odczytanych elementach
        for row in reader:
            # zapis danych z obiektów do zmiennej link
            # utworzonej z klasy Link
            link = Link(
                row["movieId"],
                row["imdbId"],
                row["tmdbId"]
            )
            # dodanie zmiennej do listy linków
            listLinks.append(link.__dict__)
    # wyświetlenie zawartości listy
    return listLinks


# strona wyświetlająca oceny filmów
@app.get("/ratings")
# funkcja wyświetlająca oceny filmów
def Ratings():
    # deklaracja listy ocen
    listLinks = []

    # ścieżka do katalogu wraz z nazwą
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # ścieżka do pliku ratings.csv
    file_path = os.path.join(BASE_DIR, "ratings.csv")

    # otwarcie pliku za pomocą ścieżki w kodie UTF-8
    # przeznaczonym tylko do odczytu jako plik
    with open(file_path, "r", encoding="utf-8") as file:
        # odczytanie pliku o rozszerzeniu csv i tworzenie słownika
        # poprzez pominięcie przecinków między słowami
        reader = csv.DictReader(file, delimiter=",")

        # pętla po odczytanych elementach
        for row in reader:
            # zapis danych z obiektów do zmiennej rating
            # utworzonej z klasy Rating
            rating = Rating(
                row["userId"],
                row["movieId"],
                row["rating"],
                row["timestamp"]
            )
            # dodanie zmiennej do listy ocen
            listLinks.append(rating.__dict__)
    # wyświetlenie zawartości listy
    return listLinks


# strona wyświetlająca tagi o filmach
@app.get("/tags")
# funkcja wyświetlająca tagi o filmów
def Tags():
    # deklaracja listy tagów
    listTags = []

    # ścieżka do katalogu wraz z nazwą
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # ścieżka do pliku tags.csv
    file_path = os.path.join(BASE_DIR, "tags.csv")

    # otwarcie pliku za pomocą ścieżki w kodie UTF-8
    # przeznaczonym tylko do odczytu jako plik
    with open(file_path, "r", encoding="utf-8") as file:
        # odczytanie pliku o rozszerzeniu csv i tworzenie słownika
        # poprzez pominięcie przecinków między słowami
        reader = csv.DictReader(file, delimiter=",")

        # pętla po odczytanych elementach
        for row in reader:
            # zapis danych z obiektów do Tag
            tag = Tag(
                row["userId"],
                row["movieId"],
                row["tag"],
                row["timestamp"]
            )
            # dodanie zmiennej do listy ocen
            listTags.append(tag.__dict__)
    # wyświetlenie zawartości listy
    return listTags
