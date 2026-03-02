## File
--File is collection of data that is availbale to a program 
-- can retrieveand use data

why use in python?
--stored data is permanent unless someone remove it
--stored data can be shared
--It is possible to update and remove the data

Two type of files
1. Text file
2. Binary File



--- File handling
mode of file -- raed , write append , exclusive


Text File -It stores data in form of characters, It is used to store characters and strings

Binary Fiel -IT stores in the form of byte a group of 8bits each. It is used to store text, image, pdf, csv, video adn audio


Mode 
1.Text Mode -- treats its content  as if it  contains text strings of the str type

2.Binary Mode -- Pyhton uses the data in file without any decoding , binary mode file reflects the rawdata in file


------IF file is not closed then python garbage collector will delete it but closeing file is best practice

--- it may lead to data curruption and insufficient memory utilizaiton





## file object

when we do open() that will provide us file object 
so if f=open() then f is file object

## modes 
-- w , r, x, a, r+ ,w+ x+ 

now w = create new file and overrides alll data
    a = create new file and append do not override
    x= create new file and write
    r+ = open for reading then writing
    w+ = open for writing then reading but overrifing
    a+ = open for wrting then reading but no overiding


# method
----writelines() == this method is used to store/write group of string (list, tuple,set) into the file representated by the file object

-- read(size) --read filw in string formate
-- readline() - to read a single line of the file
-- readlines() - to read whole file returns data with datatype 


--tell() --this method is used to find currect positon of file pointer from beginning of the file. Position starts from 0.

-- seek(position) -- This method is used to move file pointer from one position to another position from beginning of the file. Position starts from 0 and it must be positive integer.

