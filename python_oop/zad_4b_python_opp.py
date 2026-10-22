'''
Rozszerzyć skrypt z punktu 7 o przyjmowanie parametru city
, który może być przekazywany w wierszu poleceń podczas 
wykonywania (np. python main.py --city=Berlin ). Należy 
wykorzystać moduł argparse do wczytywania przekazywanych 
parametrów, a w razie przekazania wartości ograniczyć 
pobierane browary do miasta, które zostało wskazane.
'''
#Optional może ale nie musi być

from dataclasses import dataclass
from typing import Optional
import argparse
import requests

@dataclass
class Brewery:
    #deklaracja zmiennych z bazy
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[str]
    state: str
    street: Optional[str]

    def __str__(self) -> str:
        return (
            f"Browar: {self.name} \n"
            f"ID: {self.id} \n"
            f"Typ: {self.brewery_type}\n"
            f"Adres 1: {self.address_1}, {self.city}\n"
            f"Adres 2: {self.address_2}, {self.city}\n"
            f"Adres 3: {self.address_3}, {self.city}\n"
            f"City: {self.name}"
            f"State Province: {self.state_province}\n"
            f"Postal code: {self.postal_code}\n"
            f"Longitude: {self.longitude}\n"
            f"Latitude: {self.latitude}\n"
            f"Phone: {self.phone}\n"
            f"Website URL: {self.website_url}\n"
            f"State: {self.state}\n"
            f"Streer: {self.street}\n"
            #linia **********************
            f"{'*' * 20}"
        )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--city", 
        type=str, 
        help="Miasto, z którego pobrać browary")
    args = parser.parse_args()

    #adres strony
    url = "https://api.openbrewerydb.org/v1/breweries"

    params = {"per_page": 20, "page":1}
    
    if args.city:
        params["by_city"] = args.city
    #laczenie z API
    response = requests.get(
        url,
        params= params,
        timeout=10
    )

    response.raise_for_status()
    #lista słownikowa
    data = response.json()

    lista_browarow = [
        Brewery(**browar)
        for browar in data
    ]

    for browar in lista_browarow:
        print(browar)

if __name__ == "__main__":
    main()

#wyświetlanie python zad_8_typing.py --city=Berlin


