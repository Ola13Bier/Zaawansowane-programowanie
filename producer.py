"""
producer.py
Dodaje zadania do kolejki RabbitMQ.

Przykłady:
    python producer.py
    python producer.py --count 100
"""

import argparse
import json
import uuid
from datetime import datetime, timezone

import pika

RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 8081
QUEUE_NAME = "jobs"


def connect_to_rabbitmq():
    credentials = pika.PlainCredentials("guest", "guest")

    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=credentials,
    )

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(
        queue=QUEUE_NAME,
        durable=True,
    )

    return connection, channel


def add_job(channel, description: str):
    job = {
        "id": str(uuid.uuid4()),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "pending",
        "description": description,
    }

    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=json.dumps(job, ensure_ascii=False),
        properties=pika.BasicProperties(
            delivery_mode=2,
            content_type="application/json",
        ),
    )

    print(f"Dodano zadanie {job['id']}: {description}")


def main():
    parser = argparse.ArgumentParser(
        description="Dodawanie zadań do kolejki RabbitMQ."
    )

    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Liczba zadań do dodania (domyślnie: 1).",
    )

    args = parser.parse_args()

    if args.count < 1:
        parser.error("--count musi być większe od zera")

    connection = None

    try:
        connection, channel = connect_to_rabbitmq()

        for number in range(1, args.count + 1):
            add_job(
                channel,
                f"Rozmowa telefoniczna nr {number}"
            )

    finally:
        if connection is not None and connection.is_open:
            connection.close()


if __name__ == "__main__":
    main()
