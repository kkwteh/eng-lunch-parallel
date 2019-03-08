from queue import Queue
from threading import Thread
import requests
import os

def slow_fibonacci(n):
    if n in {0, 1}:
        return 1

    return slow_fibonacci(n-1) + slow_fibonacci(n-2)

def job_loop(q):
    while True:
        f, args = q.get()
        print(f(*args))
        q.task_done()

def run_parallel(num_threads=12):
    q = Queue(maxsize=0)

    for _ in range(num_threads):
        worker = Thread(target=job_loop, args=(q,))
        worker.setDaemon(True)
        worker.start()

    for _ in range(10):
        q.put((
            slow_fibonacci,
            [31]
        ))

    q.join()

if __name__ == '__main__':
    run_parallel()
