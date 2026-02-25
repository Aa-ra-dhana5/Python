from threading import Thread
from queue import Queue
import time
import random

NUMBER_OF_COOKS = 3   # 🔥 Change this to 1 and run again

order_queue = Queue()

def cook():
    while True:
        item = order_queue.get()

        if item is None:
            order_queue.task_done()
            break

        table = item
        prep_time = 3   # Fixed time so comparison is clear

        print(f"{time.strftime('%H:%M:%S')} 👨‍🍳 START Table {table}")
        time.sleep(prep_time)
        print(f"{time.strftime('%H:%M:%S')} ✅ DONE  Table {table}")

        order_queue.task_done()

# Start cooks
threads = []
for _ in range(NUMBER_OF_COOKS):
    t = Thread(target=cook)
    t.start()
    threads.append(t)

# 🔥 Auto generate 6 orders instantly
start_time = time.time()

for table in range(1, 7):
    order_queue.put(table)

# Wait for all tasks to finish
order_queue.join()

# Stop workers
for _ in range(NUMBER_OF_COOKS):
    order_queue.put(None)

for t in threads:
    t.join()

end_time = time.time()

print("\nTotal time taken:", round(end_time - start_time, 2), "seconds")