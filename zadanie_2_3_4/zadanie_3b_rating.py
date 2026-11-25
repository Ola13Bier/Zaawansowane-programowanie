# klasa rating oceniająca filmy
class Rating():
    # deklaracja zmiennych
    def __init__(self, userId, movieId, rating, timestamp):
        # identyfikator Użytkownika
        self.userId = userId
        # identyfikator filmu
        self.movieId = movieId
        # ocena
        self.rating = rating
        # kiedy film został obejrzany
        self.timestamp = timestamp
