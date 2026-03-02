## Thread

-- Process = running program
-- thread = a lightweight unit inside that process


## Lock 
- Ensures only one thread enters critical section at aa time

'''
lock = threading.Lock()
'''

## RLock
- If same thread tries to acquire same lock again → deadlock.
--Example:
Function A → calls Function B
Both use same lock.

'''lock = threading.RLock() '''

## Event
- Used for signaling between threads.One thread waits, another signals.

'''
def waiter():
    print("Waiting...")
    event.wait()
    print("Got signal!")

def setter():
    time.sleep(2)
    print("Sending signal")
    event.set()
'''

wait() → blocks
set() → releases all waiting threads
clear() → resets to False

## Condition
--Used when threads wait for some condition to become true.
Requires a lock internally.

'''
def producer():
    with condition:
        items.append(1)
        print("Produced")
        condition.notify()

def consumer():
    with condition:
        while not items:
            condition.wait()
        items.pop()
        print("Consumed")
'''
wait() → releases lock & waits
notify() → wakes one thread

# Semaphore
Controls access to limited resources.
''' 
semaphore = threading.Semaphore(3)
'''

# BoundedSemaphore
Same as Semaphore but prevents over-release.
If you release more times than acquired → error.

It prevents programming mistakes.
'''
semaphore = threading.BoundedSemaphore(3)
'''

# Queue
-queue.Queue() is already synchronized.
No need for manual locks.
Queue handles locking internally.

'''
q = Queue()

def producer():
    q.put("Item")

def consumer():
    item = q.get()
    print("Consumed:", item)
'''

## Daemon Thread
--Daemon thread runs in background.

If main thread exits → daemon thread stops automatically.

''' 
t.daemon = True
'''


### ----> If a thread:
    1.Is discarded
    2.Crashes
    3.Ends unexpectedly

👉 Locks / RLocks / Semaphores are NOT auto-released
👉 Other threads may block forever

---- Safe desing pattern
  1.Always use context manager (with) - beacuse with ensures Lock is released even if exception happens
  2.Use try-finally if manual acquire
  3.Avoid long critical sections
  4.Avoid sleeping while holding lock
  5.Use timeouts when acquiring lock