# Variable Naming Rules in Python

# Variable names cannot start with a digit; they must start with a letter (a-z, A-Z) or an underscore (_).
# Valid
valid_name = "Alice"
_valid_name = "Bob"
name1 = "Charlie"
# Invalid
# 1invalid_name = "David"  # SyntaxError: invalid syntax
# 2name = "Eve"            # SyntaxError: invalid syntax

# Variables must be assigned a value when they are created.
# Valid
age = 25
height = 175.5
# Invalid
# weight    # NameError: name 'weight' is not defined

# Python variable names are case sensitive. name and Name are considered different variables.

# It is recommended to avoid using Turkish characters (ç, ğ, ü, ö, ş, ı) in variable names. English characters are preferred.

# String literals can be enclosed in single (' ') or double (" ") quotes.
single_quote_string = 'Hello, world!'
double_quote_string = "Python is fun!"

print(single_quote_string)  # Hello, world!
print(double_quote_string)  # Python is fun!

# Multiple variables can be assigned values in one line.
x, y, z = 10, 20, 30
print(x)  # 10
print(y)  # 20
print(z)  # 30

# Invalid
# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)

# Example 1
# Variables and tax calculation
salaryAli = 5000
salaryVeli = 8000
tax = 0.15
# Ali's salary after tax
print(salaryAli - (salaryAli * tax))  # 5000 - 750 = 4250
# Veli's salary after tax
print(salaryVeli - (salaryVeli * tax))  # 8000 - 1200 = 6800

# Example 2
order1=110
order2=456
order3=728.45
print("Total :",order1+order2+order3)

# Example 3
customerName="Derya"
customerSurname="Güler"
costomerNameSurname=customerName+" "+customerSurname
customerGender=True # girl
customerIdNumber='11111111111'
customerBirthYear=2002
customeraddress='İstanbul Kadıköy'
customerAge=2024-customerBirthYear
