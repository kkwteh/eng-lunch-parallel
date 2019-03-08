from queue import Queue
from threading import Thread
import requests
import os

def save_url_response(url):
    resp = requests.get(url)
    with open(os.path.basename(url), 'wb') as f:
        f.write(resp.content)
        print(f'work done for {url}')

def job_loop(q):
    while True:
        f, args = q.get()
        f(*args)
        q.task_done()

def run_parallel(num_threads=12):
    q = Queue(maxsize=0)

    for _ in range(num_threads):
        worker = Thread(target=job_loop, args=(q,))
        worker.setDaemon(True)
        worker.start()

    with open('list-of-urls.txt', 'r') as f:
        for line in f.readlines():
            url = line.strip()
            q.put((
                save_url_response,
                [url]
            ))

    q.join()

if __name__ == '__main__':
    run_parallel()
