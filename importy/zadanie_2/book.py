# klasa opisująca książkę
class Book:
    # deklaracji zmiennych
    def __init__(self, library, title, publication_date, author_name, author_surname, number_of_page):
        # nazwa biblioteki
        self.library = library
        # tytuł książki
        self.title = title
        # data publikacji
        self.publication_date = publication_date
        # imię autora
        self.author_name = author_name
        # nazwisko autora
        self.author_surname = author_surname
        # liczba stron
        self.number_of_pages = number_of_page

    # wyswietlanie
    def __str__(self):
        return (
            f"nazwa biblioteki: {self.library} \n"
            f"tytuł: {self.title} \n"
            f"data publikacji: {self.publication_date} \n"
            f"imię autora: {self.author_name} \n"
            f"nazwisko autora: {self.author_surname} \n"
            f"liczba stron: {self.number_of_pages} \n"
            f"{'*' * 20}\n"
        )

    def __repr__(self):
        return self.__str__()
