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

11. **`split(separator)()`**
     Splits the string into a list using the specified separator.

    ```python
    text = "hello world Python"
    print(text.split(" "))  # Output: ['hello', 'world', 'Python']

12. **`join(iterable)()`**
     Joins elements of the iterable with the specified separator.

    ```python
    words = ['hello', 'world', 'Python']
    print(" ".join(words))  # Output: "hello world Python"

    
13. **`startswith(prefix)()`**
     Checks if the string starts with the specified prefix.

    ```python
    text = "hello world"
    print(text.startswith("hello"))  # Output: True
    print(text.startswith("world"))  # Output: False

14. **`endswith(suffix)()`**
      Checks if the string ends with the specified suffix.

    ```python
    text = "hello world"
    print(text.endswith("world"))  # Output: True
    print(text.endswith("hello"))  # Output: False

15. **`zfill(width)()`**
     Pads the string with zeros (0) to reach the specified width.

    ```python
    text = "42"
    print(text.zfill(5))  # Output: "00042"

16. **`format(*args, **kwargs)()`**
    Formats the string using the specified arguments. Python 3.6 and later also support f-strings (formatted string literals), but the format method is still very useful.

    ```python
    text = "My name is {} and I am {} years old."
    print(text.format("Alice", 30))  # Output: "My name is Alice and I am 30 years old."

17. **`rjust(width, fillchar)()`**
     Right-aligns the string and pads it with the specified fillchar to the specified width.

    ```python
    text = "hello"
    print(text.rjust(10, "*"))  # Output: "*****hello"
 
18. **`ljust(width, fillchar)()`**
     Left-aligns the string and pads it with the specified fillchar to the specified width.

    ```python
    text = "hello"
    print(text.ljust(10, "*"))  # Output: "hello*****"
