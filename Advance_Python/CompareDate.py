from datetime import date
d1 = date(2020 , 6 , 30 )
d2 = date(2000 , 6 , 30 )

print(d1 == d2)
print(d1 != d2)
print(d1 > d2) #True
print(d1 < d2) #False


dob = date(2005 , 5 , 15)

t=date.today()

age= t.year -dob.year - ((t.month, t.day) < (dob.month , dob.day))

print(age)