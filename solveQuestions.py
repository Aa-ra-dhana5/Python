#Age group categorization

# for age in range(0, 101):
#     if age < 13:
#         print(f"Age {age}: Child")
#     elif age < 20:
#         print(f"Age {age}: Teenager")
#     elif age < 65:
#         print(f"Age {age}: Adult")
#     else:
#         print(f"Age {age}: Senior")
        
#final answer        
i = int(input("Enter your age: "))

if i < 13:
    print("You are a Child.")   
elif i < 20:
    print("You are a Teenager.")        
elif i <50:
    print("You are an Adult.")
else : 
    print("You are a Senior.")


#2 Movie ticket pricing

age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").lower()
    
price = 12 if age >= 18 else 8

if(day == "wednesday"):
    price -=2
    
print(f"Your ticket price is: ${price}")


#3 Grade calculation

grade =int(input("Enter your grade percentage: "))

if grade < 0 or grade > 100:
    print("Invalid grade percentage. Please enter a value between 0 and 100.")
else :
    if  grade >=90:
        grade = "A"
    elif grade >=80:
        grade = "B" 
    elif grade >=70:
        grade = "C"
    elif grade >=60:
        grade = "D"
    else:
        grade = "F"
    print(f"Your letter grade is: {grade}")


#4 Determine if a fruit is ripe, overripe or unripe on its colot

fruit = input("Enter the fruit name: ").lower()
color = input("Enter the color of the fruit: ").lower()

if fruit == "banana":
    if color == "green":
        print("The banana is unripe.")
    elif color == "yellow":
        print("The banana is ripe.")
    elif color == "brown":
        print("The banana is overripe.")


#5 weather activity suggestion 

weather = input("Enter the weather condition (sunny, rainy, snowy): ").lower()

if weather == "sunny":
    print("go for walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("build a snowman")
    
    
#8 password check 

password = input("Enter your password: ")

if len(password) < 8:
    strength = "weak"
elif len(password) < 12:
    strength = "medium"
else:
    strength = "strong"
    
print(f"Your password is {strength}.")


#9 leap year checking

year = int(input("Enter a year: "))

if (year %4 == 0 and year % 100 !=0 ) or (year % 400 == 0):
    print(f"{year} is a leap year. ")
  
  
#10 Pet food recommendation

pet =input("Enter your pet type (dog, cat): ").lower()
age = int(input("Enter your pet's age: "))

if pet == "dog" :
    if age < 2:
        print("Recommended food: Puppy food")
    else:
        print("Recommended food: Adult dog food")
elif pet == "cat":
    if age >5:
        print("Recommended food: Senior cat food")
    else:
        print("Recommended food: Adult cat food")
else :
    print("Invalid pet type. Please enter 'dog' or 'cat'.")