from dataclasses import dataclass
from typing import Optional


@dataclass
class Brewery:
    # deklaracja zmiennych z bazy
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
            # linia **********************
            f"{'*' * 20}"
        )
