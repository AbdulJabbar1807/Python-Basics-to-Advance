x = 2
y = 5
z = 7
b = 2.03
print(x+z)
# Always use parenthesis for any mathematical operation.
a = (x+y)*z
print(a)
 # print(b+x) # this will perform the operation but its better not to use this as these two are two different data types.
# Instead use same data types for addition operation.
b = int(b)
print(b+x)
c = int(5.32)
print(c)
d = float(85)
print(d)
first_name = 'Abdul'
last_name = 'Jabbar'
# Operators
print(first_name + last_name) # Operator overloading.
print(z**5)
print(x**10)
print(y%2) # will provide remainder
print(y/2) # will do fraction,also provide decimal values after point.
print(y//2) # will remove decimal values after fraction.
print(x<y)
print(x < y and y < z) #print(x < y < z)
print(x == y and y < z) # print(x == y < z)

# Complex numbers
complex_num = 5 + 1j # here j represents imaginary number.
print(complex_num)
print((complex_num)*3)

# Binary,Octal,and Hexa numbers in python.
print(0b100) # Binary number
print(0o20) # Octal number
print(0xFF) # Hexal number

# Decimal number to binary,octal and hexal number's.
print(bin(5))
print(oct(6))
print(hex(7))
# shorthand method for Decimal number to binary,octal and hexal number's.
print(int('100',2))
print(int('32',8))
print(int('64',16))

# Bitwise operator's
p = 1
print(p << 1)