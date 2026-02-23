#Floating-point numbers are approximations because many decimal fractions cannot be represented exactly in binary.
#For example, the decimal number 0.1 cannot be represented exactly in binary, leading to small rounding errors in calculations.
print(0.1 + 0.2 +0.3) #0.6000000000000001


from decimal import Decimal
#To mitigate this issue, Python provides the Decimal class from the decimal module, which allows for more precise decimal arithmetic.
#internally Decimal uses a different representation that can accurately represent decimal numbers, avoiding the rounding errors associated with floating-point arithmetic.

Decimal('0.1') + Decimal('0.2') + Decimal('0.3') #Decimal('0.6')

0o20 #octal representation of 16
0x10 #hexadecimal representation of 16  
0b10000 #binary representation of 16

print(0o20) #16
print(0x10) #16 
print(0b10000) #16

print(int('46', 8)) #38
print(int('46', 16)) #70    
print(int('101', 2)) #5  // only binary numbers are allowed like 0 and 1 in the string representation.
