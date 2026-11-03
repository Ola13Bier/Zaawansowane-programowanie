"""
consumer.py
Stale sprawdza kolejkę CSV, pobiera jedno zadanie pending,
wykonuje je przez 30 sekund i oznacza jako done.

Przykład:
    python consumer.py
"""

from database import get_connection, initialize_database
import time
import os

POLL_INTERVAL = 5
JOB_DURATION = 30


def get_job():

    conn = get_connection()

    try:
        conn.execute("BEGIN IMMEDIATE")

        job = conn.execute("""
            SELECT id, description
            FROM jobs
            WHERE status = 'pending'
            ORDER BY id
            LIMIT 1
        """).fetchone()

        if job is None:
            conn.commit()
            return None

        conn.execute("""
            UPDATE jobs
            SET status = 'in_progress'
            WHERE id = ?
        """, (job[0],))

        conn.commit()

        return job

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


def finish_job(job_id):

    with get_connection() as conn:
        conn.execute("""
            UPDATE jobs
            SET status = 'done'
            WHERE id = ?
        """, (job_id,))


def process_job(job):

    job_id, description = job

    print(f"Consumer {os.getpid()} wykonuje: {description}")

    time.sleep(JOB_DURATION)

    finish_job(job_id)

    print(f"Consumer {os.getpid()} zakończył: {description}")


def main():

    initialize_database()

    print("Consumer uruchomiony...")

    while True:

        job = get_job()

        if job:
            process_job(job)

        else:
            time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()