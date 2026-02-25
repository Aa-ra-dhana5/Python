## Multitasking

 1. Process based multitasking
--Executing multiple task at same time where each task is seprate independent program 
--suitable for os level

 2. Thread based multitasking
--Executing multiple task t same time where each task is a seprate independent part of the same program is called thread based multitaking and each independent part is called thread 
-- suitable for programmatic level
exa - in word it shows error for wrong spelling


## Main Thread
--When python progeam start execute it do create one thread its self its main thread
--created by PVM



##  Creating Thread
-- Thread class of threading module is used to xreate threads.
-- To create our own thread we need to create an object of Thread Class


Ways to crate:
1. Without creating class

2. creating a thread by creating a child class to Thread class

3. creating a thread by without creating a child class to Thread class

##  Thread class Methods
-- start()  ---to start thread
-- run()   --ecery thread will run this method wehn thread is strted 
-- join() this method is used to wait till the thread completely executes the run() method
