# Creating an empty tuple
empty_tuple = ()

# Creating a single-element tuple (a comma is mandatory)
single_element_tuple = (5,)

# Creating a tuple with multiple elements
multiple_elements_tuple = (1, 2, 3)

# Creating a tuple with different data types
mixed_tuple = (1, "hello", 3.14)

# Accessing Tuple Elements
# Tuple elements can be accessed using indexing:
my_tuple = (10, 20, 30, 40, 50)

# Accessing the first element
print(my_tuple[0])  # Output: 10

# Accessing the last element
print(my_tuple[-1])  # Output: 50

# Accessing a range of elements (slicing)
print(my_tuple[1:3])  # Output: (20, 30)

# Tuple Immutability
# Tuple elements cannot be changed. This means that once a tuple is created, its elements cannot be modified:
my_tuple = (1, 2, 3)

# The following line will raise an error
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Concatenating Tuples
# You can concatenate two or more tuples to create a new tuple:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Checking for Elements in a Tuple
# You can check if a particular element is in a tuple:
my_tuple = (10, 20, 30, 40, 50)

# Element check
print(20 in my_tuple)  # Output: True
print(100 in my_tuple)  # Output: False

# Tuple Unpacking
# You can assign the elements of a tuple to individual variables:
my_tuple = (1, 2, 3)

a, b, c = my_tuple

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Tuple Functions
# Here are some built-in functions you can use with tuples in Python:
my_tuple = (10, 20, 30, 40, 50)

# Number of elements
print(len(my_tuple))  # Output: 5

# Maximum element
print(max(my_tuple))  # Output: 50

# Minimum element
print(min(my_tuple))  # Output: 10

# Count of a specific element
print(my_tuple.count(20))  # Output: 1

# Index of a specific element
print(my_tuple.index(30))  # Output: 2
