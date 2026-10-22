'''
Stworzyć klasę Student, która posiada 2 parametry 
(name i marks) oraz jedną metodę is_passed, która 
zwraca wartość logiczną, pozytywną gdy średnia ocen 
jest > 50 w przeciwnym przypadku negatywną. Następnie 
należy stworzyć 2 przykładowe obiekty klasy, tak aby
 dla pierwszego obiektu metoda zwracała true , 
 a dla drugiego false.
'''

#klasa student
class Student:
    #funkcja uruchamia się przy tworzeniu
    def __init__(self, name, marks):
        #przypisanie obiektu name
        self.name = name
        #przypisanie obiektu marks
        self.marks = marks

    #Funkcja wyświetlająca zawartość
    def __str__(self):
        #Czy uczeń zdał
        if self.is_passed:
            #tak zdał
            return f"Uczeń {self.name} zdał"
        else:
            #nie nie zdał
            return f"Uczeń {self.name} nie zdał"
            

    #pobranie wartości z obiektu
    @property
    #funckja sprawdza czy uczeń zdał
    def is_passed(self) :
        #ocena wyżej niż 50 
        if self.marks > 50:
            #tak
            return True
        else:
            #nie
            return False

#deklaracja obietku klasy karol
karol = Student("Karol", 60)
#wyswietlenie obiektu
print(karol)
#deklaracja obiektu klasy marzene
marzena = Student("Marzena", 30)
#wyświetlanie obiektu
print(marzena)