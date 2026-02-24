# Run type Polymorphism
# Duck typing is a concept in Python where the type of an object is less important than the methods it defines. If an object implements the required method, it can be used, regardless of its class.


class Duck:
    walks ='yes'
    def walk(self):
        print("Duck is walking")
        
class Hourse:
    def walk(self):
        print("Hourse is walking")
        
def myfun(obj):
    #Strong typing - if exist then work
    if hasattr(obj, 'walk'):
        obj.walk()
    
duck =Duck()

print(hasattr(duck, 'walks')) #used to check if object has that method or not
# this will check if has error or not and do not throw error if not 

myfun(duck)
# here it will check first if walk is ther then it will print else do nothing


## Method Overloading -when mwthod can perform more than one task 

''' 
# Below is not possible in pyhton 
class Myclass: 
    def sum(self, a):
        print("1st sum method", a)
        
    def sum(self):
        print("2nd sum method")
        
obj = Myclass()
obj.sum()
obj.sum(10) ## throw error 

# second writtern method will be priotrised

'''

class Myclass:
    def sum(self , a, b, c):
        s =a+ b+ c 
        return s
    def sum2(self , a=0, b= 0, c= 0): #by adding default values
        s =a+ b+ c 
        return s
    def sum3(self , *args):#by adding args or kwargs
        s=0
        for i in args:
             s+=i
        return s
    
obj= Myclass()
print(obj.sum(10 , 20,30))
print(obj.sum2(10))
print(obj.sum3(10 ,20, 30, 50 ,30))



## Method overriding

class Add:
    def result(self , a , b):
        print(f"Addition: {a+b}")
        
class Multi(Add):
    def result(self, a, b):
        super().result(a, b)
        print(f"Multiplicaiton: {a*b}")
        
multiplicaiton = Multi()
multiplicaiton.result(10, 2)


## operator Overloading -- adding two objects 

class A:
    def  __init__(self , x):
        self.x = x
    def __add__(self, new):
        sum = self.x + new.x
        return sum
    
class B:
    def __init__(self,a):
        self.x =a
        
a =A(100)
b= B(200)
print(a+b)
        