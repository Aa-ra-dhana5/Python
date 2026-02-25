#Get adn set Thread

#current_thread()
# name Property - This property is used to get or set name of the thread

from threading import Thread, current_thread

def disp():
    print("child thread object", current_thread().name)
    current_thread().name='Display Thread'
    print("new name", current_thread().name)
t =Thread(target=disp)
t.start()

print("Main thread", current_thread().name)