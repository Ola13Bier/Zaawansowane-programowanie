# klasa opisująca zamówienie
class Order:
    # deklaracja danych
    def __init__(self, employee, student, books, order_date):
        # pracownik
        self.employee = employee
        # student
        self.student = student
        # ksiazki
        self.books = books
        # data zamówienia
        self.order_date = order_date

    # wyświetlenie danych
    def __str__(self):
        lista_ksiazek = "\n".join(str(book) for book in self.books)
        return (
            f"pracownik: {self.employee} \n"
            f"student: {self.student} \n"
            f"ksiazki: {lista_ksiazek} \n"
            f"data zamówienia: {self.order_date} \n"
        )
