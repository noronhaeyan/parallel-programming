import time
from threading import Thread
import asyncio

def count():
    print("One")
    time.sleep(1)
    print("Two")
    time.sleep(1)

async def asyncio_count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)


def main():
    for _ in range(3):
        count()

async def main_asyncio():
    await asyncio.gather(asyncio_count(), asyncio_count(), asyncio_count())
        

def main_thread():
    t = [None]*3
    for i in range(3):
        t[i] = Thread(target = count)
        t[i].start()
    
    for i in range(3):
        t[i].join()



if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"sequential executed in {elapsed:0.2f} seconds.")

    start = time.perf_counter()
    main_thread()
    elapsed = time.perf_counter() - start
    print(f"threading executed in {elapsed:0.2f} seconds.")

    start = time.perf_counter()
    asyncio.run(main_asyncio())
    elapsed = time.perf_counter() - start
    print(f"threading executed in {elapsed:0.2f} seconds.")