import requests
import threading
def make_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")
# List of URLs to make requests to
urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.python.org"
]

def main():
    t = []
    for i, url in enumerate(urls):
        t.append(threading.Thread(target=make_request, args=(url,)))
        t[i].start()
    
    for i in range(len(urls)):
        t[i].join()

if __name__ == "__main__":
    main()