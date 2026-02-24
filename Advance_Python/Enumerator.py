'''
It returns an enumerate object (iterator).

Conceptually it does something like:

[(0, "apple"), (1, "banana"), (2, "mango")]
'''

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
    
# Output:  
'''
1 apple
2 banana
3 mango
'''

## interview  --Q: Why use enumerate() instead of range(len())?
#enumerate() is more readable and Pythonic. It avoids manual indexing, reduces the risk of index errors, and directly provides both index and value during iteration.
    
