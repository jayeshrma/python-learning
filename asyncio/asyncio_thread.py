import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def checkStock(item):
    print(f"Checking {item} in store...")
    time.sleep(2)
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,checkStock,"Device")
        print(result)

asyncio.run(main())