# BoundedSemaphore -- that ensures that no extra release then aquire
'''
se BoundedSemaphore:

When you want strict safety

Example: Limiting connections to a database pool

Prevent bugs where release is called too many times
'''
import threading
import time

# Only 2 threads allowed
bsem = threading.BoundedSemaphore(2)

def worker(num):
    print(f"Thread {num} waiting...")
    bsem.acquire()
    print(f"Thread {num} entered")
    time.sleep(1)
    bsem.release()
    print(f"Thread {num} left")

# Extra release example
try:
    bsem.release()  # ❌ Error! Not allowed
except ValueError as e:
    print("Error:", e)

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()