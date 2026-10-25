from brewery import *
import requests


def main():
    # adres strony
    url = "https://api.openbrewerydb.org/v1/breweries"

    # laczenie z API
    response = requests.get(
        url,
        params={"per_page": 20, "page": 1},
        timeout=10
    )

    response.raise_for_status()
    # lista słownikowa
    data = response.json()

    lista_browarow = [
        Brewery(**browar)
        for browar in data
    ]

    for browar in lista_browarow:
        print(browar)


if __name__ == "__main__":
    main()
