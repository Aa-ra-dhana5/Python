## Thread Communication
# 1. Event
''' Event object manages an internal flag that can be set to true with the set() method ans reset to false with clear() method. The wait(timeout=None) method blocks until the flag is true

initially flag is true
''' 
from threading import Event,Thread
from time import sleep

def light_switch():
    sleep(3)
    e.set()
    print('Green light on')
    sleep(5)
    print('red light on')
    e.clear()

def traffic():
    e.wait()
    while e.is_set():
        print('You can go....')
        sleep(.5)
    print("Done")
    
e= Event()

t1=Thread(target=light_switch)
t2=Thread(target=traffic)

t1.start()
t2.start()

# 2. Condiiton
'''
Condition class is used to improve speed of communication between threads the condition class object is called condition variable.

notify(n=1) //no of threads -to wake up all n threads
notify_all() // to infrm all(iterable)
wait(timeout = None) //this maethod wait until notified or unitl timeout occurs.
'''

from threading import Thread,Condition
from time import sleep

lst =[]
def produce():
    cv.acquire()
    for i in range(1, 6):
        lst.append(i)
        sleep(1)
        print(" Item produced..")
    cv.notify()
    cv.release()
    
def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    print(lst)
    
    
    
cv =Condition()
t1 = Thread(target=produce)
t2 = Thread(target=consume)

t1.start()
t2.start()

# 3. Queue
'''
The Queue class of queue module is useful to create a  queue that holds the data produced by the producer
-- we need not use locks since queue are thread safe

methods
1.put() -- used by produer to insert item sinto queue
2.get() --used by consumer to retrieve items from queue
3. empty() returns true if queue is empty else return false
4. full() -- this method return True if queue is Full else returns False.
'''

from threading import Thread
from queue import Queue
from time import sleep

class Producer:
    def __init__(self):
        self.q= Queue()
    
    def produce(self):
        for i in range(1,60):
            print("Item Produced", i)
            self.q.put(i)
            sleep(1)
            
class Consumer:
    def __init__(self, prod):
        self.prod =prod
    
    def consume(self):
        for i in range(1,6):
            print("Item Recieved", self.prod.q.get(1))
            
            
p= Producer()
c= Consumer(p)

t1 =Thread(target=p.produce)
t2 =Thread(target=c.consume)

t1.start()
t2.start()

