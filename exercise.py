# # x = 10

# # def modify():
# #    # this will thow error beasuse there is declaration without valid assignment
# #     x = x + 5 
# #     print(x)

# # modify()

# import time

# def timer(func):
#     print("printed 1")
#     def wrapper(*args, **kwargs):
#         print("printed second")
#         start = time.time()
#         print(f'Start time is {start}')
    
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"End time is {end}")
    
#         print(f"Total time taken by function is {end- start} ")
#         return result
#     return wrapper

# @timer
# def newFunc():
#     for i in range(10):
#         print("This function has print ", i)
        
# newFunc()
  

#Threading
       
# import threading

# counter = 0

# def increment():
#     global counter
#     for _ in range(10000000000):
#         counter += 1

# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(counter)


# Lock()

    
# from threading import *


# class Hotel:
#     def __init__(self):
#         print("hotel is stated now")
#         # self.l = Lock()
#         # print(f'Initial Lock status: {self.l}')
        
        
#     def cook(self, n):
#         # self.l.acquire()
#         # print(self.l)
#         print(f'Cook {n} is ready ')
#         # self.l.release()
#         # print(self.l)
        
        
# h =Hotel()
# t1 =Thread(target=h.cook , args= (1,))       
# t2 =Thread(target=h.cook , args= (2,))    

# t1.start()   
# t2.start()   


# #Rlock()
# import threading
# import time

# # Shared resource
# shared_list = []
# # Reentrant Lock
# rlock = threading.RLock()

# def inner():
#     rlock.acquire()
#     # rlock.acquire()
#     shared_list.append("inner")
#     print("first lock  : ", rlock)
#     print(f"{threading.current_thread().name} added inner")
#     # time.sleep(0.1)
#     rlock.release()
#     # rlock.release()
#     print("First Lock : ", rlock)

# def outer():
#     rlock.acquire()
#     print("second Lock : ", rlock)
#     shared_list.append("outer")
#     print(f"{threading.current_thread().name} added outer")
#     inner()  # Nested function call acquires the same lock
#     rlock.release()
#     print("second Lock : ", rlock)


# threads = []
# for i in range(3):
#     t = threading.Thread(target=outer, name=f"Thread-{i+1}")
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# print("Shared list:", shared_list)


## Semaphore

# import threading
# import time
# import random

# sem = threading.Semaphore(2)

# def func(n):
#     print(f'Thread {n} is waiting..')
#     sem.acquire()
#     print(f'thread {n} is used to print ..')
#     time.sleep(random.uniform(0.5, 1.5))
#     print(f'Thread {n} is realeased now..')
#     sem.release()
    
    
# thread = [] 
# for i in range(5):
#     t1 = threading.Thread(target=func ,args=(i+1,))
#     thread.append(t1)
#     t1.start()
    
# for t in threads:
#     t.join()
    
# print("Main program finishes")


# Demon
# import threading
# import time
# import random

# # -----------------------------
# # Daemon thread: background logging
# # -----------------------------
# def background_logger():
#     while True:
#         print("[Logger] Checking system status...")
#         time.sleep(2)  # simulate periodic logging

# # -----------------------------
# # Normal thread: critical task
# # -----------------------------
# def process_request(request_id):
#     print(f"[Request {request_id}] Started processing")
#     time.sleep(random.randint(1, 10))  # simulate work
#     print(f"[Request {request_id}] Finished processing")

# # -----------------------------
# # Main program
# # -----------------------------
# # Start daemon thread
# logger_thread = threading.Thread(target=background_logger)
# logger_thread.daemon = True  # makes it a daemon thread
# logger_thread.start()

# # Start normal threads
# request_threads = []
# for i in range(5):
#     t = threading.Thread(target=process_request, args=(i+1,))
#     request_threads.append(t)
#     t.start()

# # Wait for normal threads to finish
# for t in request_threads:
#     t.join()

# print("All requests processed. Main program exits.")
# Daemon logger stops automatically


import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(2)
    print("World")

async def main():
    await hello()

asyncio.run(main())