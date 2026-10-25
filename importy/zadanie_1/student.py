# klasa student
class Student:
    # funkcja uruchamia się przy tworzeniu
    def __init__(self, name, marks):
        # przypisanie obiektu name
        self.name = name
        # przypisanie obiektu marks
        self.marks = marks

    # Funkcja wyświetlająca zawartość
    def __str__(self):
        # Czy uczeń zdał
        if self.is_passed:
            # tak zdał
            return f"Uczeń {self.name} zdał"
        else:
            # nie nie zdał
            return f"Uczeń {self.name} nie zdał"

    # pobranie wartości z obiektu
    @property
    # funckja sprawdza czy uczeń zdał
    def is_passed(self):
        # ocena wyżej niż 50
        if self.marks > 50:
            # tak
            return True
        else:
            # nie
            return False
