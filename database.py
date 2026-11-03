# biblioteka do bazy danych
import sqlite3


# nazwa bazy danych
DB_NAME = "queue.db"


# funkcja łącząca się z nazwą bazy z odświeżeniem 30
def get_connection():
    # zwracanie połączenia
    return sqlite3.connect(DB_NAME, timeout=30)


# stworzenie baz danych
def initialize_database():
    # użyj metody get_connection jako conn
    with get_connection() as conn:
        # wykonaj polecenie utworzenia tabeli jobs jeśli nie istnieje
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)


if __name__ == "__main__":
    # uruchom funkcję i utwórz tabelę
    initialize_database()
    # wyświetl komunikat
    print("Baza danych została utworzona.")
