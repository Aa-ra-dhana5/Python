list1 =[10, 20, 3 ,40]
# print(max(list1))

tupl1 = (10 ,2 ,40,30)
# print(max(tupl1))

dict = {'one':10, 'two' : 2}
# print(max(dict))  # It checks ascii code of keys and compare it
# print(max(dict, key=dict.get)) # key based values comparison
# print(max(dict.values())) #value returns

set1 = { 1, 2, 30, 4 ,5, 10}
# print(max(set1))


# Comprehension of list
squeres = [ i*i for i in range(5)]
print(squeres)

squeresdict = {i:i*i for i in range(5)}
print(squeresdict)

squereset = {i*i for i in range(5)}
print(squereset)



#event number in list
even = [ i for i in range(1,6) if i%2==0]
print(even)

#create list of cubes from 1 to 10 
cubes =[i**3 for i in range(1, 11)]
print(cubes)

#create list of length of each word
str = 'this is new me'
lenth = [len(i) for i in str.split(" ")]
print(lenth)


#swap keys and values
dict4 = {'one' : 1 , 'two':2}
dict5 = {j:i for i,j in dict4.items()}
print(dict5)


#dublicate miss data
d = {"x":1, "y":2, "z":1}

new = {v:[k for k,val in d.items() if val==v] for v in set(d.values())}

print(new)

#dictionaly ofr word adn lengh
str1= 'This is arena on air'

another = {v:len(v) for v in str1.split(" ")}
print(another)