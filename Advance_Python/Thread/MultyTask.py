## Multitasking using multi threading

from threading import Thread

class Restorant:
    def __init__(self, t):
        self.t = t
    
    def food(self):
        for i in range(1,6 ):
            print(self.t, i)
            
h1 = Restorant("Take Order From Table ")
h2 = Restorant("Serve to table : ")

t1 =Thread(target=h1.food)
t2 =Thread(target=h2.food)
t1.start()
t2.start()


##there can be issue that order will be served before it taken from the table so instead of using thread better approch is to use queue or event method 



# from threading import Thread
# from queue import Queue
# import time

# order_queue = Queue()

# class Restaurant:

#     def take_order(self):
#         for i in range(1, 6):
#             print("Taking order from table:", i)
#             order_queue.put(i)   # Put order into queue
#             time.sleep(1)

#     def serve_food(self):
#         for i in range(1, 6):
#             order = order_queue.get()  # Wait until order available
#             print("Serving food to table:", order)
#             order_queue.task_done()
#             time.sleep(1)

# r = Restaurant()

# t1 = Thread(target=r.take_order)
# t2 = Thread(target=r.serve_food)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

## in above case forst order will taken and then served


from threading import Thread
from queue import Queue
import time
import random

order_queue = Queue()

class Restaurant:

    def take_order(self):
        for i in range(1, 6):
            time.sleep(random.uniform(0.5, 1.5))  # random delay
            print("Taking order from table:", i)
            order_queue.put(i)

    def serve_food(self):
        for _ in range(1, 6):
            order = order_queue.get()  # waits only if empty
            time.sleep(random.uniform(0.5, 2))
            print("Serving food to table:", order)
            order_queue.task_done()

r = Restaurant()

t1 = Thread(target=r.take_order)
t2 = Thread(target=r.serve_food)

t1.start()
t2.start()

t1.join()
t2.join()