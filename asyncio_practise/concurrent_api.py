"""
You have a list of user IDs: [1, 2, 3, 4, 5]
Write an async function that fetches data for all users concurrently.
Each fetch takes random time between 0.5-2 seconds.

Requirements:
- All fetches should run concurrently (not sequentially)
- Return a list of all user data
- Measure and print total execution time

Expected time: ~2 seconds (not ~7.5 seconds)
"""
import asyncio
import random
import time

async def fetch_user_data(user_id):
    delay = random.uniform(0.5, 2)
    
    print(f"Fetching data for user id: {user_id} ...")
    try:
        await asyncio.wait_for(asyncio.sleep(delay), 1.5)
        print(f"Procured data for user id: {user_id} in {delay}s")
    except TimeoutError as e:
        print(f"Could not fetch data for user_id: {user_id} due to 1.5s timeout.", e)
        return


async def main():
    user_ids = [1, 2, 3, 4, 5]
    await asyncio.gather(*(fetch_user_data(i) for i in user_ids))

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"==> Total time taken: {end-start}s")