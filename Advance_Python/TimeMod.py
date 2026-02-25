# import time


# epoch = time.time()
# print(epoch)


print(time.time())
print(time.ctime())


print(time.localtime())
stobj = time.localtime()
print(stobj.tm_year)

from datetime import timedelta
delta = timedelta(
    days=2,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
# Only days, seconds, and microseconds remain
print(delta) #16 days, 8:05:56.000010 -- 2days  + 2 week day -14day = 16days

          
          
          
          


from datetime import date
print(date(2003, 12, 29).isocalendar())

print(date(2004, 1, 4).isocalendar())

# Python program to
# demonstrate time class









from datetime import time

# calling the constructor
my_time = time(12, 14, 36)

print("Entered time", my_time)

# calling constructor with 1
# argument
my_time = time(minute = 12)
print("\nTime with one argument", my_time)

# Calling constructor with
# 0 argument
my_time = time()
print("\nTime without argument", my_time)

# Creating Time object
Time = time(12,24,36,1212)

# Converting Time object to string
Str = Time.isoformat()
print("String Representation:", Str)
print(type(Str))

Time = "12:24:36.001212"

# Converting string to Time object
Time = time.fromisoformat(Str)
print("\nTime from String", Time)
print(type(Time))
