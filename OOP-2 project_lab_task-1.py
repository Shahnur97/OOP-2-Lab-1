# Writing the first python programe of my python journey.

print("I am Mohammad Shah Nur")

# Comments in python: Object Oriented Programming II Lab.

name = "Shah Nur"
print(name) 

# Python variable.

# An integer assignment
age = 23

# A floating point
salary = 20000.5

# A string
name = "Shah Nur"

print(age)
print(salary)
print(name)

# Phython Data Type.

x = "Tiger" # string
x = 20  # integer
x = 30.5  # float
x = 4j  # complex
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple
x = {"name": "Masud", "age": 23} # dict
x = {"geeks", "for", "geeks"} # set
x = True  # bool
x = b"Geeks" # binary

# Python Input/Output.

val = input("Enter your value: ") 
print(val) 

# Python Operator.
  # Arithmetic Operators.

a = 10
b = 7
add = a + b 

sub = a - b 

mul = a * b 

mod = a % b 

p = a ** b 
print(add) 
print(sub) 
print(mul) 
print(mod) 
print(p) 

  #Logical Operators.

a = True
b = False
print(a and b) 
print(a or b) 
print(not a) 

  #Bitwise Operators.

a = 17
b = 7
print(a & b) 
print(a | b) 
print(~a) 
print(a ^ b) 
print(a >> 2) 
print(a << 2) 

  #Assignment Operators.

a = 12
b = a 
print(b) 
b += a 
print(b) 
b -= a 
print(b) 
b *= a 
print(b) 
b <<= a 
print(b)

# Python If Else.

i = 20
if (i < 15): 
    print("i is smaller than 15") 
    print("i'm in if Block") 
else: 
    print("i is greater than 15") 
    print("i'm in else Block") 
print("i'm not in if and not in else Block") 

# Python For Loop.

for i in range(0, 10, 2): 
    print(i) 

# Python While Loop.

# Python program to illustrate while loop 
count = 0
while (count < 3): 
    count = count + 1
    print("Hello Daffodil")

# Python Functions.

# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)