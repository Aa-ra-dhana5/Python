# import threading

# t=threading.current_thread().name
# print(t) #main thread

# print("Hellow")


## creating thread
# 1.witohut creating class

from threading import Thread



# def func(name):
   
#     print("This is thread class of name : ", name)
    
# thredobj =Thread(target=func, args=("shariyan",))
# thredobj.start()




#Example two
## child thread is invoke by main thread and execution of each thread is independent and not ordered can change the sequence



def disp():
    for i in range(5):
         print("child Thread")
    
t = Thread(target = disp)
# t.start()

# for i in range(5):
#     print("Main Threas")
    
    
# 2. Creating a thread by creating a child class to Thread class
# object of this class will be thread object


# class Mythread(Thread):
#      pass

# t = Mythread()
# print(t.name)

## Thread Methods

# run() and start() methods
# class NEWthread(Thread):
#      def run(self): # run method is override - only runs when start method was called
#          print("Run method")

# t1 = NEWthread()
# t1.start()  

# print(t1.name)

#join() method -- helps tpo run all one thread at time like all child thread will run toghether and then other thread will run
# t1.join()
    
    
## 2. Thread child class with constructor

# class Thread1(Thread):
#     def __init__(self):
#         Thread.__init__(self) # this is required
#         print("Child claass Thread")
        
#     def run(self):
#         pass
    
# t3 = Thread1()
# t3.start()
# print("Main Thread")

## why call thread constructor 
'''
The Thread class (from the threading module) sets up:

_target

_args

_kwargs

_started

_ident

_tstate_lock

If constructor not called → these attributes don't exist → .start() fails.
'''
#"When subclassing Thread, we must call the parent constructor using super().init() because the Thread class performs essential internal initialization required for thread lifecycle management. Without calling it, the thread object is not properly constructed and calling start() will raise a RuntimeError."




##3  Creating a thread without creating a child class to Thread class

class NewClass:
    def __init__(self):# here we do not need start() method beacuse it runs on main thread
        print("Thread whothout child class")
        
    def disp(self):
        print("display the thread with start()")

obj = NewClass()
thread_obj = Thread(target= obj)

## to access disp we need start to run thread beacuse its not running on main thread its new thread now
disp_thread = Thread(target=obj.disp())
disp_thread.start()

