import asyncio
import aiofiles
import time

def read_file_sync(filename):
    with open(filename, 'r') as f:
        return f.read()

def read_multiple_files_sync(filenames):
    results = []
    for filename in filenames:
        content = read_file_sync(filename)
        results.append(content)
    return results

async def read_file_async(filename):
    async with aiofiles.open(filename, 'r') as f:
        return await f.read()

async def read_multiple_files_async(filenames):
    # All files read concurrently!
    tasks = [read_file_async(filename) for filename in filenames]
    return await asyncio.gather(*tasks)

# Comparison
async def compare():
    filenames = [f'file{i}.txt' for i in range(20)]
    
    # Sync version
    start = time.time()
    sync_results = read_multiple_files_sync(filenames)
    # print(sync_results)
    print(f"Sync: {time.time() - start}s")
    
    # Async version
    start = time.time()
    async_results = await read_multiple_files_async(filenames)
    print(f"Async: {time.time() - start}s")

asyncio.run(compare())