"""
producer.py
Dodaje zadania do kolejki CSV ze statusem pending.

Przykłady:
    python producer.py
    python producer.py --count 100
"""

import argparse
import csv
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path

from filelock import FileLock

QUEUE_FILE = Path(__file__).with_name("queue.csv")
LOCK_FILE = Path(str(QUEUE_FILE) + ".lock")
FIELDS = ["id", "created_at", "status", "description"]


def ensure_queue_exists():
    with FileLock(str(LOCK_FILE)):
        if not QUEUE_FILE.exists() or QUEUE_FILE.stat().st_size == 0:
            with QUEUE_FILE.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=FIELDS)
                writer.writeheader()


def add_job(description: str):
    job = {
        "id": str(uuid.uuid4()),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "pending",
        "description": description,
    }

    # Blokada chroni przed równoczesnym zapisem/odczytem przez inne procesy.
    with FileLock(str(LOCK_FILE)):
        file_exists = QUEUE_FILE.exists() and QUEUE_FILE.stat().st_size > 0
        with QUEUE_FILE.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            if not file_exists:
                writer.writeheader()
            writer.writerow(job)

    print(f"Dodano zadanie {job['id']}: {description}")


def main():
    parser = argparse.ArgumentParser(description="Dodawanie zadań do kolejki.")
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Liczba zadań do dodania (domyślnie: 1).",
    )
    args = parser.parse_args()

    if args.count < 1:
        parser.error("--count musi być większe od zera")

    ensure_queue_exists()
    for number in range(1, args.count + 1):
        add_job(f"Rozmowa telefoniczna nr {number}")


if __name__ == "__main__":
    main()
