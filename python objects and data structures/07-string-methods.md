# String Methods in Python

Python provides a variety of string methods for manipulating and processing strings. Here are some essential string methods and how to use them:

1. **`upper()`**
   Converts all characters in the string to uppercase.

   ```python
   text = "hello"
   print(text.upper())  # Output: "HELLO"

2. **`lower()`**
   Converts all characters in the string to lowercase.

   ```python
   text = "HELLO"
   print(text.lower())  # Output: "hello"

capitalize()
Capitalizes the first character of the string and makes the rest lowercase.
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

title()
Capitalizes the first character of each word in the string.
text = "hello world"
print(text.title())  # Output: "Hello World"

strip()
Removes whitespace characters from the beginning and end of the string.
text = "  hello  "
print(text.strip())  # Output: "hello"
