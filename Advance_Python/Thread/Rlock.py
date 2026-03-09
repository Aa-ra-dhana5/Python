#2. Rlock --A reentatnt lock is synchronization primitive that may be acquired multiple times by the same thread
#A reetrant loc must be released by the thread that aquired it ,,, once thread has acquired a reetant lock , the same thread may acquire it again without blocking



from threading import *

class Flight:
    def __init__(self , availalable_seat):
        self.availalable_seat = availalable_seat
        self.l =RLock() #Rlock object
        print(self.l)
        
    def reserve(self, need_seat):
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
