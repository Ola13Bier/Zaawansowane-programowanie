# klasa film
class Movie:
    # deklaracja danych
    def __init__(self, movieId, title, genres):
        # identyfikator filmu
        self.movieId = movieId
        # tytuł filmu
        self.title = title
        # gatunek filmu
        self.genres = genres
