# klasa opisująca tag
class Tag():
    # deklaracja zmiennych
    def __init__(self, userId, movieId, tag, timestamp):
        # identyfikator użytkownika
        self.userId = userId
        # identyfikator filmu
        self.movieId = movieId
        # tagi opisujące film
        self.tag = tag
        # kiedy został obejrzany
        self.timestamp = timestamp
