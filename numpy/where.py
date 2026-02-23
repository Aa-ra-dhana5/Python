#where() function is use dto create a new Array which contains returned element chosen from expression1 or expression2 depending on condition. If condition is true expression1 is execured else expression@
#numpy.where(condition, expression1, expression2)

from numpy import *
a=array([99, 2, 0, 4, 5 ,6])
b=array([99,98,97,96,95,94])
# c=where(a<b, a,b)
# print(c)


#nonzero Function -- Function to determine the position of elemtn which are non zero 
#this will return an array that contains the index of the element od the arrau which are not equals to zero
#nonzero(a)
# print(type(nonzero(a))) #-- tuple


#Alising array
old_array = array([101, 102, 103,104])
new_array = old_array
#print(new_array is old_array) #True
#now here new_array is old_array

#View method and copy mehtod -- like shallow copy
#view() - used to construct a new view of array with the same data of existing array -- the existing array and new array will share diffrent memory locaitons
# if a new array modifiec the existing will also be modified as the elements in both the arrays will be like mirror image

# n =a.view()
# print("a", id(a))
# print("n", id(n))
# n[0] =200
# print(n)
# print(a)


#copy method = used to create a copy of an existing array . If the new array get modified the existing array awill not be affected 

m=a.copy()
m[1] =300
print(m)
print(a)
