import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"Encrypted data: {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,encrypt,"Secret-Message")
        print(result)

if __name__=="__main__":
    asyncio.run(main())
    
asyncio.run(main())