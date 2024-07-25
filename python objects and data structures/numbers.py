# There are two main numeric data types in Python: int (integer) and float.
# int represents whole numbers. float represents decimal numbers.

# Simple arithmetic operations and data types
print(9 + 5)  # integer + integer, result: 14
print(67 - 66)  # integer - integer, result: 1
print(4 + 0.8)  # integer + float, result: 4.8

# To get the type of a value from the output;
print(type(2))  # <class 'int'>
print(type(2.85))  # <class 'float'>

# To determine the order of operations in the expression we wrote, we can use parentheses.
# In Python, the order of operations is determined by mathematical rules: first multiplication and division, then addition and subtraction.
print(4 + 6 * 5 + 2)  # 4 + 30 + 2 = 36
print((4 + 6) * (5 + 2))  # (10) * (7) = 70

# In Python, the result of any arithmetic operation between an int and a float is a float.
# Examples
a = 5    # int
b = 3.2  # float

print(a + b)   # 8.2, addition
print(a - b)   # 1.8, subtraction
print(a * b)   # 16.0, multiplication
print(a / b)   # 1.5625, division
print(a ** b)  # 172.46660197362375, exponentiation
print(a % b)   # 1.7999999999999998, modulus
print(a // b)  # 1.0, floor division

# Examples of floor division
print(-15 // 4)   # -4
print(15 // 4)    # 3
print(-15 // -4)  # 3
print(15 // -4)   # -4
