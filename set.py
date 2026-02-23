#Set

#create set
a = set()
a.add('New')
# print(a)

# a.update('a', 'b')
# print(a)

#remove or delet set

# a={101 , 10, 'new'}
# print(a)
# #a.remove(10)#returns error if element do not exist
# a.discard(10)#do not throw any error
# print(a)


#accessing set
a3 ={ 101 , 120 , 'new' , 'one'}
for i in a3:
    print(i)
    
a3.clear() # clearing set
print(a3)


#getsizeof() function returns size of an object in bytes
from sys import *
print(getsizeof(a))