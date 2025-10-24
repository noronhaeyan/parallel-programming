import asyncio
import time
import random

async def fetch_user(user_id: int):
    delay = random.uniform(0.25, 2)
    print(f"Fetching user with user_id: {user_id} ...")
    await asyncio.sleep(delay)
    user = {'user_id': user_id, "User": f"User{user_id}"}
    print(f"Found user {user} with user_id {user_id} with delay {delay}")
    return user

async def fetch_posts(user: dict):
    delay = random.uniform(0.25, 2)
    print(f"fetching posts from {user['User']} ...")
    await asyncio.sleep(delay)
    posts = [f"Post {i} by {user['User']}" for i in range(1, 3)]
    print(f"Post coro for {len(posts)} posts by {user['User']}"
          f" (done in {delay}s)")
    for i in range(2):
        print(f"-{posts[i]}" ) 

async def fetch_user_and_post(user_id: int):
    user = await fetch_user(user_id)
    await fetch_posts(user)

async def main():
    start = time.perf_counter()
    await asyncio.gather(*(fetch_user_and_post(i) for i in [1,2,3]))
    end = time.perf_counter()
    print(f"\n==> Total time: {end - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
