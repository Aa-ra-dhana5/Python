# f =open('student.txt', mode='w')
# f.write("Hello How are you")
# f.close()


# f =open('student.txt', mode='r')
# print(f)
# f =open('student.txt', mode='rb')
# print(f)

#userd when file not exist then creatioin with write
# f =open('student.txt', mode='x')
# print(f)

# file object
# this are method ot check about file
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)


# isfile() method -- path module method

# import os 
# print(os.path.isfile('student.txt'))


# writeline() method
# for this we can use w mode or a mode  -if wants to append then a and if wants to write then w  
# lst=['rahul\n' , 'shreyansh\n' , 'vary']
# f =open('student.txt', mode='w')

# f.writelines(lst)

#read(size) - read string in text mode and bytes in bianry mode
#size - is number of bytes if not defines then read whole file

# f =open('student.txt', mode='r')
# data = f.read()
# print(data) 
'''
rahul
shreyansh
vary
'''


# data1 = f.readline() #read a single line
# print(data1) #rahul



# data1 = f.readlines() #read a full file with no new line with '\n' too
# print(data1) # ['rahul\n', 'shreyansh\n', 'vary']
# f.close()

#tell() method

f =open('student.txt', mode='r')
print(f.tell()) #0
data2 = f.read(5)
print(data2)
print(f.tell()) #5

# seek(position) -- to move file pointer

print(f.seek(3))