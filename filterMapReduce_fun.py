#filter() function  - returns a list
#filer(function_name , iterable)

list2 =[10 ,93 ,68 ,50 ,60]

# def highmark(n):
#     if n>= 60 :
#         return True
    
    
# b= filter(highmark, list2)# its in filter object formate
# b1= list(filter(highmark, list2))#in list object formate
# b2= list(filter(lambda n: (n<60), list2))#using lambda function

# for i in b1:
#     print(i)
    
    
#map()  -returns a list
#map(fun_name , iterable)

# mapResult = list(map(lambda x: x+1 , list2))

# for i in mapResult:
#     print(i)


#Reduce -- returns a single value

from functools import reduce

reducefun= reduce(lambda n, m : n+m , list2)
print(reducefun)
