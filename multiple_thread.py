from threading import Thread
import threading
import random
import time

def print_names():
    delay = random.uniform(2,4)
    time.sleep(delay)
    current_thread = threading.current_thread()
    print(f"Hello from thread: {current_thread.name} ...")

def main():

    N = 5
    t = [None]*N

    for i in range(N):
        t[i] = Thread(target=print_names)
        t[i].start()

    for i in range(N):
        t[i].join()

    current_thread = threading.current_thread()
    print(f"Hello from thread: {current_thread.name} ...")

if __name__ == "__main__":
    main()