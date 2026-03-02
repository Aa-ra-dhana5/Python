# # Semaphore
# '''
# Manage an internal counter -- deverement by  acquire() and oncreament by each release() call
# when counter is zero aquire() wait till thread calls release()
# '''

'''
Use Semaphore:

When you have N resources, but accidental extra release won’t break program

Example: Limiting API calls
'''


# from threading import *

# class Flight:
#     def __init__(self , availalable_seat):
#         self.availalable_seat = availalable_seat
#         self.l =Semaphore(3) #semaphore object -- 3 thread at a time
#         print(self.l)
        
#     def reserve(self, need_seat):
#         self.l.acquire()
#         print(self.l._value)
#         print('Available seat: ', self.availalable_seat)
#         if(self.availalable_seat >= need_seat):
#             name = current_thread().name
#             print(f'{need_seat} seat is alloted for {name}')
#             self.availalable_seat -=need_seat
#         else:
#             print("sorry! all seats are alloted")
#         self.l.release() 
#         # print(self.l._value)
           
# f = Flight(2)
# t1 =Thread(target=f.reserve, args=(1, ), name="Rahul")
# t2 =Thread(target=f.reserve, args=(1, ), name="Sonham")
# t3 =Thread(target=f.reserve, args=(1, ), name="Ketki")
# t4 =Thread(target=f.reserve, args=(1, ), name="Mohan")
# t3.start()        
# t1.start()        
# t2.start()        
# t4.start()        



#example : 
import threading
import time

# Only 2 threads allowed at a time
sem = threading.Semaphore(2)

def worker(num):
    print(f"Thread {num} waiting to enter...")
    with sem:  # acquire automatically
        print(f"Thread {num} entered critical section")
        time.sleep(2)
        print(f"Thread {num} leaving")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()