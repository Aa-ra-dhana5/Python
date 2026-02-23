#Genrators are functions that return a sequence of values
#Yield returns the element frmo genetator function  into genetato object
#next()  function is used to map element in yield object


def dip(a, b):
    yield a
    yield b
    
result = dip(10, 20)#type is genrater 
print(next(result))
print(next(result))


# result1 = list(result)
# print(result1)






# def infinite_counter():
#    n = 0
#    while True:
#        yield n
#        n += 1
# # Using the generator
# counter = infinite_counter()
# for _ in range(10):
#    print(next(counter), end=" ")