# klasa link
class Link():
    # deklaracja danych
    def __init__(self, movieId, imdbId, tmdbId):
        # identyfikator filmu
        self.movieId = movieId
        # identyfikator obcy z bazy danych imdb
        self.imdbId = imdbId
        # identyfikator obcy z bazy danych tmdb
        self.tmdbId = tmdbId       
