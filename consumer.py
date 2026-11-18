"""
consumer.py
Oczekuje na zadania z RabbitMQ,
wykonuje każde zadanie przez 30 sekund
i potwierdza jego przetworzenie (ACK).

Przykład:
    python consumer.py
"""

import json
import os
import socket
import time

import pika

RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 8081
QUEUE_NAME = "jobs"

JOB_DURATION_SECONDS = 30


def connect_to_rabbitmq():
    credentials = pika.PlainCredentials("guest", "guest")

    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=credentials,
        heartbeat=600,
        blocked_connection_timeout=300,
    )

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(
        queue=QUEUE_NAME,
        durable=True,
    )

    # Jeden consumer pobiera maksymalnie jedno niepotwierdzone zadanie.
    channel.basic_qos(prefetch_count=1)

    return connection, channel


def process_job(job):
    print(
        f"[{socket.gethostname()}:{os.getpid()}] "
        f"Rozpoczynam zadanie {job['id']}: "
        f"{job['description']}",
        flush=True,
    )

    # Symulacja wykonywania zadania.
    time.sleep(JOB_DURATION_SECONDS)

    print(
        f"[{socket.gethostname()}:{os.getpid()}] "
        f"Zakończono zadanie {job['id']}",
        flush=True,
    )


def callback(channel, method, properties, body):
    try:
        job = json.loads(body.decode("utf-8"))

        process_job(job)

        # Potwierdzenie poprawnego przetworzenia wiadomości.
        channel.basic_ack(
            delivery_tag=method.delivery_tag
        )

    except Exception as exc:
        print(
            f"Błąd podczas przetwarzania zadania: {exc}",
            flush=True,
        )

        # Wiadomość wraca do kolejki.
        channel.basic_nack(
            delivery_tag=method.delivery_tag,
            requeue=True,
        )


def main():
    worker = f"{socket.gethostname()}:{os.getpid()}"

    connection = None

    try:
        connection, channel = connect_to_rabbitmq()

        print(
            f"Consumer {worker} uruchomiony. "
            "Oczekuję na zadania...",
            flush=True,
        )

        channel.basic_consume(
            queue=QUEUE_NAME,
            on_message_callback=callback,
            auto_ack=False,
        )

        channel.start_consuming()

    except KeyboardInterrupt:
        print("\nConsumer zatrzymany.", flush=True)

    finally:
        if connection is not None and connection.is_open:
            connection.close()


if __name__ == "__main__":
    main()
