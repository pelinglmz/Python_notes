# Numeric Data Types and Operations in Python

## Numeric Data Types

There are two main numeric data types in Python: `int` (integer) and `float`. 
- **`int`** represents whole numbers.
- **`float`** represents decimal numbers.

## Simple Arithmetic Operations and Data Types

int + int results in int.

int + float results in float.

```python
print(9 + 5)  # integer + integer, result: 14
print(67 - 66)  # integer - integer, result: 1
print(4 + 0.8)  # integer + float, result: 4.8
```
Use type() to determine the type of a value.

```python

# Getting the Type of a Value
print(type(2))  # Output: <class 'int'>
print(type(2.85))  # Output: <class 'float'>

```

Order of Operations :

In Python, the order of operations follows mathematical rules: first multiplication and division, then addition and subtraction. Parentheses can be used to control the order of operations.

```python
print(4 + 6 * 5 + 2)  # 4 + 30 + 2 = 36
print((4 + 6) * (5 + 2))  # (10) * (7) = 70
```
Type Conversion in Arithmetic Operations :

In Python, the result of any arithmetic operation between an int and a float is a float.

(floor division) returns the largest integer less than or equal to the result of the division.

```python
a = 5    # int
b = 3.2  # float

print(a + b)   # 8.2, addition
print(a - b)   # 1.8, subtraction
print(a * b)   # 16.0, multiplication
print(a / b)   # 1.5625, division
print(a ** b)  # 172.46660197362375, exponentiation
print(a % b)   # 1.7999999999999998, modulus
print(a // b)  # 1.0, floor division

# Examples of Floor Division
print(-15 // 4)   # -4
print(15 // 4)    # 3
print(-15 // -4)  # 3
print(15 // -4)   # -4
```
