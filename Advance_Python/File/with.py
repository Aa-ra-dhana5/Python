# used to open file -open a file using with statement there is no need to close the file explicitly.

with open('student.txt') as f:
    data =f.read()
    print(data)
    print(f.closed)
    
print(f.closed)