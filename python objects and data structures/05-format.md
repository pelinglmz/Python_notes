# String Formatting in Python

The ways of formatting strings using the format method and f-strings in Python:

```python
name = "Nazım"
surname = "Hikmet"

# Using positional arguments with format
print("My name is {} {}".format(name, surname))
# Output: My name is Nazım Hikmet
# Explanation: {} placeholders are replaced with the first and second arguments in format.

print("My name is {0} {1}".format(name, surname))
# Output: My name is Nazım Hikmet
# Explanation: {0} and {1} placeholders correspond to the first and second arguments, respectively.

print("My name is {1} {0}".format(name, surname))
# Output: My name is Hikmet Nazım
# Explanation: {1} and {0} switch the positions of the arguments, so the surname comes first.

print("My name is {n} {s}".format(n=name, s=surname))
# Output: My name is Nazım Hikmet
# Explanation: Named placeholders {n} and {s} are replaced by corresponding keyword arguments.

print("My name is {s} {n}".format(n=name, s=surname))
# Output: My name is Hikmet Nazım
# Explanation: Named placeholders switch the positions of the name and surname.

print("My name is {} {} and I am {} years old".format(name, surname, 36))
# Output: My name is Nazım Hikmet and I am 36 years old
# Explanation: Multiple placeholders are replaced by corresponding arguments in order.

age = 38
print(f"My name is {name} {surname} and I am {age} years old.")
# Output: My name is Nazım Hikmet and I am 38 years old.
# Explanation: f-strings (formatted string literals) embed expressions directly inside string literals.

result = 300 / 850
print('The result is {}'.format(result))
# Output: The result is 0.35294117647058826
# Explanation: {} placeholder is replaced with the result of the division.

# Formatting with precision and width
print("The result is {r:1.3}".format(r=result))
# Output: The result is 0.353
# Explanation: {r:1.3} formats the result to 3 decimal places.
# `1` specifies the minimum width, but in this case, the number is shorter than the width, so it has no effect.

print("The result is {r:10.3}".format(r=result))
# Output: The result is       0.353
# Explanation: {r:10.3} formats the result to 3 decimal places and provides a total width of 10 characters.
# Spaces are added on the left of the number to meet the width requirement.
