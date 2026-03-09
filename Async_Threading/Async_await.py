import time
import threading

def fetch_data(name):
    print(f"Fetching {name}...")
    time.sleep(10)
    print(f"{name} done")

start = time.time()


apis = ["API 1", "API 2", "API 3","API 4","API 5","API 6","API 7","API 8","API 9"]
threads = []


for api in apis:
    t = threading.Thread(target=fetch_data, args=(api,))
    t.start()
    threads.append(t)

# t2 = threading.Thread(target=fetch_data, args=("API 2",))
# t3 = threading.Thread(target=fetch_data, args=("API 3",))
# t2.start()
# t3.start()
for t in threads:
    t.join()

# t2.join()
# t3.join()
threadtime = time.time() - start
print("Threading Time:", threadtime)




import asyncio
import time

async def fetch_data(name):
    print(f"Fetching {name}...")
    await asyncio.sleep(10)
    print(f"{name} done")

async def main():

    start = time.time()

    await asyncio.gather(
        fetch_data("API 1"),
        fetch_data("API 2"),
        fetch_data("API 3"),
        fetch_data("API 4"),
        fetch_data("API 5"),
        fetch_data("API 6"),
        fetch_data("API 7"),
        fetch_data("API 8"),
        fetch_data("API 9")
    )
    asyncawaitTime = time.time() - start
    print("Async Time:", asyncawaitTime)
asyncawaitTime = time.time() - start

asyncio.run(main())

if (threadtime > asyncawaitTime):
    print(threadtime-asyncawaitTime)

