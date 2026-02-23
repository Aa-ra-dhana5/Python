# f = open('new.py')
# print(f.readline())


# for line in open('new.py'):
#     print(line ,end='')


# f = open('new.py')
# while True:
#     line = f.readline()
#     if not line : break
#     print(line)

#iter object

mylist = [ 1, 2, 3, 4]
I =iter(mylist)
print(I)

I.__next__()
print(I)

f= open('new.py')

print(iter(f) is f) #for file its true


mynewList = [1, 2, 3]
print(iter(mynewList) is mynewList) #false

#file stored in variable is itself itratable object 
#but not list 


D= {'a' : 1 , "b" : 2}
I = iter(D)
print(I) # this will provid eme iteratbale objects memory refrece where it will start

R = range(5)
I = iter(R)
#iteratable
