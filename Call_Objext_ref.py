#pass/call by object refrence

#Immutable
def val(x):
    x=15
    print(x, id(x))


x=10
val(x)
print(x, id(x))


#Mutable
def list1(lst):
    print("Before append in function: ", lst , id(lst))
    lst.append(4)
    print("Inside functon : ", lst, id(lst))
    
lst =[ 1 , 2 , 3]
list1(lst)
print("Before append: ", lst , id(lst))