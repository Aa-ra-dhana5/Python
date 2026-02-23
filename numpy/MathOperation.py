
from numpy import *

a=array([99, 2, 3, 4, 5 ,6])
b=array([99,98,97,96,95,94])
# c=a+b
# for val in c:
#     print(val)


# print(a != b)


#any() and all() function 
#any() this function will return true if any one of element of the iterable is true
#all() when all are true

print(all(a==b)) #False
print(any(a==b)) #True