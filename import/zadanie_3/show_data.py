import base_data as bd


def ShowOnlyEvenNumber():
    evenNumber = []
    for i in bd.numbers:
        if i % 2 == 0:
            evenNumber.append(i)
    evenNumber.sort()
    print("Liczba parzysta: ", evenNumber)
