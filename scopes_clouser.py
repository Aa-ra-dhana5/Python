# fucntional scope 
# and item inside function are accessable by funciton itself 
# but globle scope cannot access funcitonal scope value


# username="new"

# def names():
#     username = "functionName"
#     print(username)
# print(username)
# names()

# x= 10 

# def fglobalName():
#     global x
#     x=22

# fglobalName()
# print(x)


#clouser :A function remembers the variables from its outer (enclosing) scope, even after the outer function has finished executing.

#It works because of Python’s LEGB rule (Local → Enclosing → Global → Built-in scope).

#LEGB Rule
# EGB tells Python where to look for a variable name.
# When you use a variable, Python searches in this exact order:
# L → E → G → B

# 1️⃣ L = Local
# Variables inside the current function.

# 2️⃣ E = Enclosing
# Variables in the outer function (if function is nested).

# 3️⃣ G = Global
# Variables defined at the top level of the file.

# 4️⃣ B = Built-in
# Predefined names like print, len, int, etc.

#Climbing is process when the inner funciton has no vwlue for the variable it do try to check from parents 

# x=11
# def f1():
#     x=22
#     def f2():
#         print(x)
#     f2()
# f1()

#returning defination of f2()
#factory functions
# def f1():
#     x=22
#     def f2():
#         print(x)
#     return f2
# f1()
# myresult =f1()
# myresult()

#bag theory
# now storing defination doent means it stores only the two line code of f2()
# behind the scene it stores
# 1. code 2. globals  3.closure
   
   
#another exmple of factory function

def values(num):
    def another(x):
        return x ** num
    return another

f1 =values(3)
print(f1(2))
print(f1)

