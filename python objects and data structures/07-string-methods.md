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

6. **`lstrip()`**
   Removes whitespace characters from the beginning of the string.

   ```python
   text = "  hello"
   print(text.lstrip())  # Output: "hello"

7. **`rstrip()`**
   Removes whitespace characters from the end of the string.

   ```python
   text = "hello  "
   print(text.rstrip())  # Output: "hello"

8. **`replace(old, new)()`**
   Replaces occurrences of the substring old with the substring new.

   ```python
   text = "hello world"
   print(text.replace("world", "Python"))  # Output: "hello Python"

9. **`find(substring)()`**
    Returns the index of the first occurrence of the substring substring. Returns -1 if the substring is not found.
   
   ```python
   text = "hello world"
   print(text.find("world"))  # Output: 6
   print(text.find("Python"))  # Output: -1

10. **`rfind(substring)()`**
    Returns the index of the last occurrence of the substring substring. Returns -1 if the substring is not found.

   ```python
   text = "hello world world"
   print(text.rfind("world"))  # Output: 12
