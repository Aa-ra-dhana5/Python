list_first = [1, 2, 3, 4, 5]



#print(list_first[1])
#print(list_first[0 : 3])
#print(list_first[0: 5: 2])

list_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(list_fruits[1 : 2])

#list_fruits[1 : 2] = "papita"
#print(list_fruits) #['apple', 'p', 'a', 'p', 'i', 't', 'a', 'cherry', 'date', 'elderberry']

list_fruits[1 : 2] = ["papita"]
print(list_fruits) #['apple', 'papita', 'cherry', 'date

print(list_fruits[1 :1]) #[]
list_fruits[1 :1] = ["test", "test"]
print(list_fruits) #['apple', 'test', 'test', 'papita', 'cherry', 'date', 'elderberry']


# insert nothing operation or deletion operation
list_fruits[1 :3] = []
print(list_fruits) #['apple', 'papita', 'cherry', 'date', 'elderberry']

#loop
for fruit in list_fruits:
    print(fruit)
    
    
#if statement
if "papita" in list_fruits:
    print("papita is in the list")
    
    
#append
list_fruits.append("fig")
print(list_fruits) #['apple', 'papita', 'cherry', 'date', 'elderberry', 'fig']

#pop
print(list_fruits.pop()) #fig
print(list_fruits) #['apple', 'papita', 'cherry', 'date', 'elderberry']

#remove
print(list_fruits.remove("papita")) 
print(list_fruits) #['apple', 'cherry', 'date', 'elderberry']

#insert
list_fruits.insert(1, "grape")
print(list_fruits) #['apple', 'grape', 'cherry', 'date', 'elderberry']

#rerence change fundamental
fruits_samerefrence = list_fruits
fruite_diffretrefrence = list_fruits.copy()

#list comprehension -means creating a new list by applying an expression to each item in an iterable
squared_numbers = [x**2 for x in range(1, 6)]
print(squared_numbers) #[1, 4, 9, 16, 25

another_expression = [x**2 + 2 for x in range(1, 6)]
print(another_expression) #[3, 6, 11, 18, 27]


#Copy and cloning
#copy -- .copy() and slice() ----(cloning) method bothe are used 
#creates new list but they are independent of each other

a1 = [ 1, 2 , 3 ]
a2 =a1.copy()

a3=a1[:]
print(a2)
print(a3)
