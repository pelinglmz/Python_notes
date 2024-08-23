# Python Data Types and Type Conversion

In Python, data types define the kind of value a variable can hold. Common data types include integers (`int`), floating-point numbers (`float`), strings (`str`), and booleans (`bool`). Type conversion allows you to change a value from one data type to another.

### 1. Input and Type Checking

```python
x = input('1.sayı: ')
y = input('2.sayı: ')

# (input() returns strings by default)
print(type(x))  # Output: <class 'str'> 
print(type(y))  # Output: <class 'str'>

# Convert input strings to integers and add them
sum = int(x) + int(y)  

print(sum)  
```

input() returns values as strings (str).

To perform arithmetic operations, we need to convert these strings to integers using int().

### 2. Type Conversion
```python
x = 5               # int
y = 2.5             # float
name = 'Çınar'      # str
isOnline = True     # bool

# Type Conversion Examples

# int to float
x = float(x)
print(x)           # Output: 5.0
print(type(x))     # Output: <class 'float'>

# float to int
y = int(y)
print(y)           # Output: 2
print(type(y))     # Output: <class 'int'>

# int to str
result = str(x) + str(y)
print(result)      # Output: '5.02'
print(type(result))  # Output: <class 'str'>

# bool to str
isOnline = str(isOnline)
print(isOnline)    # Output: 'True'
print(type(isOnline))  # Output: <class 'str'>

# bool to int
isOnline = False
isOnline = int(isOnline)
print(isOnline)    # Output: 0 (False is converted to 0)
print(type(isOnline))  # Output: <class 'int'>
```

int to float: Converts an integer to a floating-point number.

float to int: Converts a floating-point number to an integer (fractional part is discarded).

int to str: Converts integers to strings for concatenation.

bool to str: Converts boolean values to their string representation.

bool to int: Converts boolean values to integers (True to 1, False to 0).

Circle Area and Circumference Calculation

```python
# To calculate the area and circumference of a circle, use the following formulas:
# Area: πr²
# Circumference: 2πr


# In the given code, the radius (r) is provided by the user.

pi = 3.14

# Prompt the user to input the radius
r = float(input("Radius: "))

# Calculate the area of the circle
area = pi * (r ** 2)
print(type(area))  # Output: <class 'float'>

# Calculate the circumference of the circle
circumference = 2 * pi * r
print(type(circumference))  # Output: <class 'float'>

# Print the results
print("Area: " + str(area) + " Circumference: " + str(circumference))

