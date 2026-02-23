# defining lambda function and IIFE

# a = lambda x: x**2+x
# print(a(2))

# passing lambda function 

def show(a1):
    print(a1(2))

show(lambda x: x)

# returnning lambda function

def returning():
     return lambda x: x
 
a3= returning()
print(a3(3))




#IIFE -Immediately invoked function expression

(lambda x:print(x+1))(5)