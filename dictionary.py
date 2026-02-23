#dictonaty used to store data in key value pair

my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict) #{'name': 'John', 'age': 30, 'city': 'New York'}

print(my_dict.get("name")) #John

my_dict["age"] = 31
print(my_dict) #{'name': 'John', 'age': 31, 'city


#loop -- shows only keys
for data in my_dict:
    print(data) #name, age, city
    #can access values using keys
    print(data, my_dict[data]) #name John, age 31, city New York
    
    
#or we can access each item in dictonary

for key, vlaue in my_dict.items():
    print(key, vlaue) #name John, age 31, city New York
    
#if in dictonary
if "name" in my_dict:
    print("name is in the dictonary") #name is in the dictonary     
    

print(len(my_dict)) #3

#add new key value pair
my_dict["country"]  = "India"
print(my_dict) #{'name': 'John', 'age': 31, 'city': 'New York', 'country': 'India'}

#pop
print(my_dict.pop("age")) #31

#popitems
print(my_dict.popitem()) #('country', 'India')

print(my_dict) #{'name': 'John', 'city': 'New York'}

#delete

del my_dict["city"]
print(my_dict) #{'name': 'John'}

newuserdatat = my_dict.copy()
print(newuserdatat) #{'name': 'John'}

newuserdatat["age"] = 30

print(newuserdatat) #{'name': 'John', 'age': 30}
print(my_dict) #{'name': 'John'}


#dictonary in dictonary

newDict = {"name" : {"first" : "mariyah" , "last" : "khan"} , "Age" : 30}
print(newDict) #{'name': {'first': 'mariyah', 'last': 'khan'}, 'Age': 30}

 #dictionaty has list ? 
 #list_Dict = { "list1" : "[1,2,3]"}
#print(list_Dict) #{'list1': '(1, 2,3,4)'} #indentationerror beacuse of wrong list format in dictionary
list_Dict = { "list1" : [1,2,3,4]}
print(list_Dict) #{'list1': [1, 2, 3, 4]}

tuple_Dict = { "tuple1" : (1,2,3,4)}
print(tuple_Dict) #{'tuple1': (1, 2, 3, 4)}

#square of numbers using dictionary comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(squared_dict.clear()) #None

#fromkeys 
keys = ["a", "b", "c"]
value = 0   
new_dict = dict.fromkeys(keys, value)
print(new_dict) #{'a': 0, 'b': 0, 'c': 0}

#keys() --- returns all the keys
print(new_dict.keys()) #dict_keys(['a', 'b', 'c'])
#now to access element convert to list

#values()
print(new_dict.values()) #dict_values([0, 0, 0])
#convert to list to access element

#update()
new_dict.update({"D" : 0})
print(new_dict)


#setdefault() method to return value of the specific key
#If key is not found then it inserts ley with the specified valie

print(new_dict.setdefault('m')) #if value is not given then none assings as value
print(new_dict.setdefault('n', 3))
print(new_dict)