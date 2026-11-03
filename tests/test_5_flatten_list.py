# przyjmuje listę i zwraca ją spłaszczoną
def flatten_list(nested_list: list) -> list:
    # lista pusta
    result = []

    # pętla for po elementach listy
    for element in nested_list:
        # czy element jest instancją listy
        if isinstance(element, list):
            # wywołanie ponownie funkcji
            result.extend(flatten_list(element))
        else:
            # dodanie do listy
            result.append(element)
    # zwróć wynik
    return result
