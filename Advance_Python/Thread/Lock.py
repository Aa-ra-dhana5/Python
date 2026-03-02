# thread synchronization


#1 Lock 
'''
acquire(blocking =True ,timeout =1)
release() -unlock the lock
'''

from threading import *

class Flight:
    def __init__(self , availalable_seat):
        self.availalable_seat = availalable_seat
        self.l =Lock() #lock object
        print(self.l)
        
    def reserve(self, need_seat):
        #if blocking =flase it will show the error of access lock before realease
        # similarly when it takes time more than 2 sec it shows the same error add sleep() and check
        self.l.acquire()
        self.l.acquire()
        print(self.l)
        print('Available seat: ', self.availalable_seat)
        if(self.availalable_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.availalable_seat -=need_seat
        else:
            print("sorry! all seats are alloted")
        self.l.release() 
        self.l.release() 
        print(self.l)
           
f = Flight(2)
t1 =Thread(target=f.reserve, args=(1, ), name="Rahul")
t2 =Thread(target=f.reserve, args=(1, ), name="Sonham")
t3 =Thread(target=f.reserve, args=(1, ), name="Ketki")
t3.start()        
t1.start()        
t2.start()        
