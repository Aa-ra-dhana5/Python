# import numpy
from numpy import *
#1D array

#using array()

array_name = numpy.array([101 ,102, 103])
array_name = array([101 ,102, 103])
print(array_name)
print(type(array_name))

#define array using linspace
#linespace( start, end, num =50 , enpoint =True) -- devides in 50 parts default value we can change it 
another = linspace( 1 , 8 )
print(another.dtype)


#define array using logspace
#logsapce(start, stop , num =50 , endpoint =True , base =10.0 , dtype =None, axis =0) -- becomes base^start to base^stop  num is to devide in parts 
# new_arr = logspace(1, 3)
# print(new_arr)

#defineing array using arange() function 
#arange(start, stop, stepsize, dtype=None) --- stepsize  is spce between two value

# arange1= arange(1, 10, 2)
# print(arange1)


#zeros method -array with 0
#zeros(shape , dtype = float , order='C) order == 'c' == roq and 'f' is column 
# a = zeros(6 , dtype = int)
# print(a)

#ones method -aeeay woth 1s
#ones(shape, dtype=float, order = 'C)
# b=ones(6, dtype =int)
# print(b)
