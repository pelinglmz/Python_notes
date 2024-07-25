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

3. **`capitalize()`**
   Capitalizes the first character of the string and makes the rest lowercase.

   ```python
   text = "hello world"
   print(text.capitalize())  # Output: "Hello world"

4. **`title()`**
   Capitalizes the first character of each word in the string.

   ```python
   text = "hello world"
   print(text.title())  # Output: "Hello World"

5. **`strip()`**
   Removes whitespace characters from the beginning and end of the string.

   ```python
   text = "  hello  "
   print(text.strip())  # Output: "hello"
