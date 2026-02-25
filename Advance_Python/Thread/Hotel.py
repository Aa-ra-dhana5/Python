from threading import Thread
from queue import Queue
import time
import random

# Queues
order_queue = Queue()
ready_queue = Queue()

# Cook worker
def cook():
    while True:
        table, food = order_queue.get()
        prep_time = random.uniform(2, 5)

        if table.lower() != '' and food.lower() != '':
            print(f"\n👨‍🍳 Cooking {food} for Table {table} (takes {prep_time:.2f}s)")
            time.sleep(prep_time)
            ready_queue.put((table, food))
            order_queue.task_done()
        else:
            return

# Server worker
def serve():
    while True:
        table, food = ready_queue.get()
        print(f"\n🍽 Serving {food} to Table {table}")
        ready_queue.task_done()

# Start cook threads (1 cook)
for _ in range(3):
    Thread(target=cook, daemon=True).start()

# Start server thread
Thread(target=serve, daemon=True).start()

print("🍴 Restaurant System Started")
print("Type 'exit' to stop\n")

# Main loop (taking orders)
while True:
    table = input("\nEnter table number: ").strip()

    if table.lower() == "exit":
        break

    if not table:
        print("⚠ Table number required!")
        continue

    # Only reaches here if table is valid
    food = input("Enter food item: ").strip()

    if not food:
        print("⚠ Food item required!")
        continue

    print(f"\n📝 Order received: Table {table} ordered {food}")
    order_queue.put((table, food))

print("Closing restaurant...")