from brewery import *
import argparse
import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--city",
        type=str,
        help="Miasto, z którego pobrać browary")
    args = parser.parse_args()

    # adres strony
    url = "https://api.openbrewerydb.org/v1/breweries"

    params = {"per_page": 20, "page": 1}

    if args.city:
        params["by_city"] = args.city
    # laczenie z API
    response = requests.get(
        url,
        params=params,
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


# wyświetlanie python zad_8_typing.py --city=Berlin
if __name__ == "__main__":
    main()
