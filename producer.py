"""
producer.py
Dodaje zadania do kolejki CSV ze statusem pending.

Przykłady:
    python producer.py
    python producer.py --count 100
"""

from database import get_connection, initialize_database
import argparse

def add_job(description):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO jobs (description, status) VALUES (?, ?)",
            (description, "pending")
        )

    print(f"Dodano zadanie: {description}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=1)
    args = parser.parse_args()

    initialize_database()

    for i in range(1, args.count + 1):
        add_job(f"Rozmowa telefoniczna nr {i}")


if __name__ == "__main__":
    main()
