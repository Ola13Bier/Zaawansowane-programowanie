'''
Stworzyć endpoint, który zwraca
respone {'hello': 'world'}, uruchomić
serwer i sprawdzić w przeglądarce czy
endpoint zwraca odpowiednie dane.
'''
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"hello": "world"}
