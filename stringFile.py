

characters = 'string'

sliced_characters = characters[0:8]
hoping_character= characters[0:7:2]

#print(characters)
#print(repr(sliced_characters))
#print(hoping_character)
#print(len(characters))

#lower() and upper() methods
print(characters.lower())   
print(characters.upper())

#strip() method
string_with_spaces = '   string with spaces   '
print(string_with_spaces)
print(string_with_spaces.strip())

#replace() method
print(characters.replace('s', 'S'))

#string to list
characters  = "one, two, three"
characters_listwithspaces = characters.split()
characters_list = characters.split(', ')
#print(characters_list)  #doesnt include , and  spaces
#print(characters_listwithspaces) #includes, 


#find() method
findding = " Finding char in a string"
print(findding.find('char'))  #returns the index of the first occurrence of 'char'

#count() method 
couting = ' Hello parapata patapata new parapata'
print(couting.count('parapata'))  #returns the number of occurrences of 'parapata'

#formatting strings
name = 'Arvanya'
age = 25
greeting = 'Hello, my name is {} and I am {} years old.'
print(greeting.format(name, age))

#list to string
characters_list = ['one', 'two', 'three']
characters_string = ', '.join(characters_list)
print(characters_string)

# for loop 
#for char in characters:
 #   print(char)
    
#double quotes maintain
bigString = "he said, \"Hello!\""
print(bigString)

#join
list_of_strings = ['Hello', 'World', 'Python']
joined_string = ' '.join(list_of_strings)


#raw string
raw_string = r'This is a raw string with a backslash: \n'
print(raw_string)

path_string = r'C:\Users\Arvanya\Documents'
print(path_string)

# or using doube forwared slash
path_string2 = 'C:\\Users\\Arvanya\\Documents'
print(path_string2)
