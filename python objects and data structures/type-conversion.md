# Python Data Types and Type Conversion

## Introduction

In Python, data types define the kind of value a variable can hold. Common data types include integers (`int`), floating-point numbers (`float`), strings (`str`), and booleans (`bool`). Type conversion allows you to change a value from one data type to another.

## Examples and Explanations

### 1. Input and Type Checking

```python
x = input('1.sayı: ')
y = input('2.sayı: ')

print(type(x))  # Output: <class 'str'> (input() returns strings by default)
print(type(y))  # Output: <class 'str'>

toplam = int(x) + int(y)  # Convert input strings to integers and add them

print(toplam)  # Output: sum of x and y as integers

Explanation:

input() returns values as strings (str).
To perform arithmetic operations, we need to convert these strings to integers using int().

2. Type Conversion
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

Explanation:

int to float: Converts an integer to a floating-point number.
float to int: Converts a floating-point number to an integer (fractional part is discarded).
int to str: Converts integers to strings for concatenation.
bool to str: Converts boolean values to their string representation.
bool to int: Converts boolean values to integers (True to 1, False to 0).
