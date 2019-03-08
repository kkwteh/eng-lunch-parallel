import requests
import os

def save_url_response(url):
    resp = requests.get(url)
    with open(os.path.basename(url), 'wb') as f:
        f.write(resp.content)
        print(f'work done for {url}')

def run_serial():
    with open('list-of-urls.txt', 'r') as f:
        for line in f.readlines():
            save_url_response(line.strip())

if __name__ == '__main__':
    run_serial()
