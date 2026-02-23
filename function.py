#recursion
import sys
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())


#1.1Printing

# def square(n):
#     print(n**2)

# n =int(input("enter number: "))
# square(n)


#1.2return Value

# def square(n):
#     return (n**2)

# n=int(input("Enter value :"))
# result = square(n)
# print(result)

#2 funciton with multiple param

# def intro(name , age):
#     print(f" i am {name}, my age is {age}")

# intro("Aaradhana", 20)

#3 plumorphism in function s
#write a function multiply that twwo number, but also accept and multiply string

# def multiply(n1, n2):
#     return (n1 * n2)

# result =multiply(8 , 8 )
# print(result)

# result2 = multiply('a' , 8)
# print(result2)


#4 function returning multiple values
#Create a function that returns both the area and circumference of  a circle given its radius

# def Circle(r):
#     area = 3.14 * (r * r)
#     circum = 2 * 3.14 * r
#     return area , circum

# a, c = Circle(150000)

# print(f"area is : {a:.2f} and circumference is : {c:.2f}")


#5 greet user with default if not given

# def greet(name = "user"):
#     return "hello , " + name + " !"

# print(greet())
# print(greet("Purv"))

#6 Lembda function  to create cube og number

# cube = lambda x: x**3
# print(cube(3))


#7 *args

# def sum_all(*args):
    
#     return sum(args)

# print(sum_all(1 , 2 , 3))
#print(*args)  has type none -- returns values
#print(args)   has type none -- returns tuple
# args ate iteratable so can handle by itratable tools like - for 


#8 handle multiple values in argument to make key value pair

# def key_kwargs(**kwargs):
#      for key , value in kwargs.items():
#          print(f"{key} : {value} ")
# key_kwargs(name= "Shardul" , lue = "rahse")

#9 use yeild
#yeild store memory refrence of the loop element to trace when we are exaclty

def returnvalues(limit):
    for i in range(2 , limit+1 , 2):
        return i
    
# print(returnvalues(10))# here i m getting only on evalue beacuse its returning 
# # so we user yeild to hold that value  to make sure we could move after the last point we reach in 

def returnvalues(limit):
    for i in range(2 , limit+1 , 2):
        yield i
        
for num in returnvalues(10):
    print(num)
    
    
#10 Recursion -factorial

def fact(n):
    if n== 0:
        return 1
    else:
        return n*fact(n-1)

print(fact(3))
