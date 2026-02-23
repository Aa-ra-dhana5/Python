#1 Counting Positive Numbers

# numbers = [1, -2, 3, 4, -5, 6]
# count =0

# for i in numbers:
#     if(i > 0):
#         count+=1
# print(count)    

#2 Sum of Even Numbers

# n = int(input("Enter a number: "))
# sum =0
 
# for i in range(n +1):
#     if(i%2 ==0):
#         sum += i
        
# print(f"The sum of even numbers from 0 to {n} is: {sum}")

#3 print the multiplicaton table fot a given number upto 10 but skip the fifth iteration

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     if(i == 5):
#         continue
#     print(f"{num} x {i} = {num * i}")


#4 Reverse String

# S = input("Enter a string: ")
# reversed_string = ""

# for char in S:
#     reversed_string = char + reversed_string
    
# print(f"The reversed string is: {reversed_string}")


#5 find first non repeating character in a string

# repeatedString = input("Enter a string: ")

# for char in repeatedString:
#     if(repeatedString.count(char) == 1):
#         print(char)
#         break

#6 factorial of number

# n = int(input("Enter a number: "))
# fact = 1

# while n>1:
#     fact *= n
#     n-=1
# print(f"The factorial is: {fact}")
        
        
#7 ask user to enter number till it comes in 1 to 10

# while True:
#     n = int(input("Enter a number between 1 and 10: "))
#     if 1 <= n <= 10:
#         print(f"you entered : {n}")
#         break
#     else:
#         print("Invalid input. Please try again.")
        

#8 print prime numbers 

# n= int(input("Enter a number: "))
# is_prime = True 

# for x in range(2 , n+1):
#     if (n%x == 0  and x != n):
#         is_prime = False
#         break
    
# print(is_prime)

#check uniqueness of list

#method1
# list1 = [1, 2, 3, 2, 5]

# for i  in list1 : 
#     if list1.count(i) > 1:
#         print("repeating number is : " ,i)
#         break
    
#method2
# list1 = [1, 2, 3, 2, 5]

# uniqueNumber = set()

# for n in list1:
#     if n in uniqueNumber:
#         print("repeating number is : " ,n)
        
#     else:
#         uniqueNumber.add(n)
        
# print(uniqueNumber)    
    
    
#10 exponantial time

import time

wait_time = 1
attempts = 0
max_retries = 5

while attempts < max_retries:
    print(f"Attempt {attempts + 1}: Waiting for {wait_time} seconds...")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

