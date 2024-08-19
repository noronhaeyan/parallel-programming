import os
from queue import Queue
from threading import Lock, Thread
from urllib import request

website_queue = Queue()
data_queue = Queue()
file_lock = Lock()

root = "/Users/noronhaeyan/Developer/parallel programming/code/parallel programming/downloads/"
if not os.path.exists(root):
    os.makedirs(root)


def download_data():
    while True:
        var = website_queue.get()
        if var is None:
            break
        response = request.urlopen(var)
        data = response.read()
        data_queue.put(data)


def save_data():
    while True:
        var = data_queue.get()
        if var is None:
            break
        with file_lock:
            i = 0
            while os.path.exists(root + f"website_data_{i}.dat"):
                i += 1
            open(root + f"website_data_{i}.dat", "w").close()
        with open(root + f"website_data_{i}.dat", "wb") as f:
            f.write(var)


website_list = [
    "https://www.wikipedia.org/",
    "https://nl.wikipedia.org/",
    "https://de.wikipedia.org/",
    "https://fr.wikipedia.org/",
    "https://pt.wikipedia.org/",
    "https://it.wikipedia.org",
    "https://ru.wikipedia.org",
    "https://es.wikipedia.org",
    "https://en.wikipedia.org",
    "https://ja.wikipedia.org",
    "https://zh.wikipedia.org",
]

for ws in website_list:
    website_queue.put(ws)

threads_download = []
threads_save = []
for i in range(3):
    t = Thread(target=download_data)
    t.start()
    threads_download.append(t)
    t2 = Thread(target=save_data)
    t2.start()
    threads_save.append(t2)

for i in range(3):
    website_queue.put(None)

for t in threads_download:
    t.join()

for i in range(3):
    data_queue.put(None)

for t in threads_save:
    t.join()
print(f"Finished downloading {len(website_list)} websites")
