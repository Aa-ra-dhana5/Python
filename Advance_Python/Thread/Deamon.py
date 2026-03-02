## Daemon runs always in background
'''
None daemon thread terminates, all other terminates automatically
'''

## Create Daemon 
'''
1. setDaemon(True) Method or daemon= true
t1.setDaemon(True)
or
t1.daemon =True

--t1.daemon is also used to check whether the thread is deamon or not
'''

# from threading import Thread
# def disp():
#     print('Daemon Thread')
    
# t1 =Thread(target=disp)
# print('Before : ',t1.isDaemon())

# # canbe changes only before thread start
# t1.setDaemon(True)
# #or
# #t1.daemon =True
# print('After :',t1.isDaemon())

# t1.start()


# # Main Thread is Non daemon thread
# '''
# Rest of the threads inherits from child thread

# When last non daemon thread terminates automatically all daemon will be terminated.
# '''

# import threading

# def child():
#     print("Child daemon:", threading.current_thread().daemon)

# def parent():
#     print("Parent daemon:", threading.current_thread().daemon)
#     t = threading.Thread(target=child)
#     t.start()
#     t.join()

# p = threading.Thread(target=parent)
# p.daemon = True
# p.start()
# p.join()


## In python it stops running when all the execution by non daemon thread so when i do t1.daemon is false then it will proint the rest of session even after eaxm but when i do true means t1 is deamon so it do not executes after main finihses as main thread is nondeam so daemon follows nonDaemon if it finishes then it do not run further

from threading import Thread, current_thread

from time import sleep
print("initial Thread : ", current_thread().name)
def teacher():
    for i in range(1,11):
        print('Teaching Session ' , i)
        sleep(1)
        
t1  = Thread(target = teacher)
# t1.daemon =True
t1.start()
print("Who is t1? :", t1.name)
print(f"is t1 demon? : {t1.daemon}")
sleep(6)
print("Exam Finished: ", current_thread().name)
