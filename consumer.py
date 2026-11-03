"""
consumer.py
Stale sprawdza kolejkę CSV, pobiera jedno zadanie pending,
wykonuje je przez 30 sekund i oznacza jako done.

Przykład:
    python consumer.py
"""

import csv
import os
import socket
import tempfile
import time
from pathlib import Path

from filelock import FileLock

QUEUE_FILE = Path(__file__).with_name("queue.csv")
LOCK_FILE = Path(str(QUEUE_FILE) + ".lock")

POLL_INTERVAL_SECONDS = 5
JOB_DURATION_SECONDS = 30
FIELDS = ["id", "created_at", "status", "description"]


def read_jobs():
    if not QUEUE_FILE.exists():
        return []
    with QUEUE_FILE.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_jobs_atomically(jobs):
    """Zapis do pliku tymczasowego i podmiana CSV, aby nie zostawić częściowego pliku."""
    fd, temp_name = tempfile.mkstemp(
        prefix="queue_", suffix=".csv", dir=QUEUE_FILE.parent
    )
    try:
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(jobs)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp_name, QUEUE_FILE)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def claim_one_job():
    """
    Atomowo wybiera i oznacza jedno zadanie jako in_progress.
    Blokada sprawia, że inni consumerzy nie pobiorą tego samego zadania.
    """
    with FileLock(LOCK_FILE):
        jobs = read_jobs()

        for job in jobs:
            if job["status"] == "pending":
                job["status"] = "in_progress"
                write_jobs_atomically(jobs)
                return job

    return None


def mark_job_done(job_id):
    with FileLock(LOCK_FILE):
        jobs = read_jobs()
        for job in jobs:
            if job["id"] == job_id:
                job["status"] = "done"
                write_jobs_atomically(jobs)
                return True
    return False


def process_job(job):
    print(
        f"[{socket.gethostname()}:{os.getpid()}] "
        f"Rozpoczynam zadanie {job['id']}: {job['description']}",
        flush=True,
    )

    time.sleep(JOB_DURATION_SECONDS)

    if mark_job_done(job["id"]):
        print(
            f"[{socket.gethostname()}:{os.getpid()}] "
            f"Zakończono zadanie {job['id']}",
            flush=True,
        )


def main():
    worker = f"{socket.gethostname()}:{os.getpid()}"
    print(f"Consumer {worker} uruchomiony. Oczekuję na zadania...", flush=True)

    while True:
        try:
            job = claim_one_job()

            if job is not None:
                process_job(job)
            else:
                time.sleep(POLL_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            print("\nConsumer zatrzymany.", flush=True)
            break
        except Exception as exc:
            print(f"Wystąpił błąd: {exc}", flush=True)
            time.sleep(POLL_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
