website = "https://www.torproject.org/"
course = "Cybersecurity Training: From Beginner to Advanced"

# 1- Remove the leading and trailing whitespace characters from the string ' Hello World '.
result = ' Hello World '.strip()
result = ' Hello World '.lstrip()  # Removes only leading whitespace characters
result = ' Hello World '.rstrip()  # Removes only trailing whitespace characters

# 2- Remove the characters ':htps' from the string 'https://www.torproject.org/'
result = website.lstrip('/:htps')
print(result)

# Remove every character except for 'torproject.org' from 'www.torproject.org'
result = 'www.torproject.org'.strip('w.moc')
print(result)

# 3- Convert all characters in the 'course' string to lowercase.
result = course.lower()
print(result)
# Convert all characters in the 'course' string to uppercase.
result = course.upper()
print(result)
# Capitalize the first letter of each word in the 'course' string.
result = course.title()
print(result)

# 4- How many 'a' characters are in the 'website' string?
result = website.count('a')
print(result)
# How many times does 'www' appear in the 'website' string?
result = website.count('www')
print(result)
# How many times does 'www' appear in the first 10 characters of the 'website' string?
result = website.count('www', 0, 10)
print(result)

# 5- Does the 'website' string start with 'www' and end with 'com'?
print(website.startswith('www'))  # False
print(website.startswith('https'))  # True
print(website.endswith('com'))  # False

# 6- Is the '.org' substring present in the 'website' string?
result = website.find('.org')  # Returns the index of the first occurrence of '.org'. Returns -1 if not found.
print(result)  # Output: 23

result = website.find('.org', 0, 10)  # Searches for '.org' in the first 10 characters of 'website'.
print(result)  # Output: -1 ('.org' is not found in the first 10 characters)

result = course.find('Cybersecurity')  # Returns the index of the first occurrence of 'Cybersecurity' in 'course'.
print(result)  # Output: 0 (because 'Cybersecurity' is at the beginning of the 'course' string)

result = course.rfind('Cybersecurity')  # Returns the index of the last occurrence of 'Cybersecurity' in 'course'.
print(result)  # Output: 0 (because 'Cybersecurity' is at the beginning of the 'course' string and there is only one occurrence)

result = website.index('.org')  # Returns the index of the first occurrence of '.org'. Raises a ValueError if not found.
print(result)  # Output: 23

result = website.rindex('.org')  # Returns the index of the last occurrence of '.org'. Raises a ValueError if not found.
print(result)  # Output: 23

# result = website.rindex('.comm')  # This would raise a ValueError as '.comm' is not found.
# print(result)  # This line would raise a ValueError when uncommented.

# 7- Are all characters in the 'course' string alphabetic? (isalpha, isdigit)
result = course.isalpha()  
print(result)  # Output: False
# `course.isalpha()` checks if all characters in `course` are alphabetic.
# Since `course` contains spaces, colons (:), and other special characters, the result is False.

result = 'Hello'.isalpha()  
print(result)  # Output: True
# Since 'Hello' contains only alphabetic characters, the result is True.

result = course.isdigit()  
print(result)  # Output: False
# `course.isdigit()` checks if all characters in `course` are numeric.
# Since `course` contains alphabetic characters and spaces, the result is False.

result = '123'.isdigit()  
print(result)  # Output: True
# Since '123' contains only numeric characters, the result is True.

# 8- Center the 'Contents' string in a field of 10 characters wide and pad with '*' on both sides.
result_center = 'Contents'.center(10, '*')
print("Center:", result_center)  # Output: '**Contents**'

# Left-align the 'Contents' string in a field of 10 characters wide and pad with '*' on the right side.
result_ljust = 'Contents'.ljust(10, '*')
print("Left Just:", result_ljust)  # Output: 'Contents***'

# Right-align the 'Contents' string in a field of 10 characters wide and pad with '*' on the left side.
result_rjust = 'Contents'.rjust(10, '*')
print("Right Just:", result_rjust)  # Output: '***Contents'

# 9- Replace all spaces in the 'course' string with '-'.
result = course.replace(' ', '-')
print(result)
# Replace the first 5 spaces in the 'course' string with '-'.
result = course.replace(' ', '-', 5)
print(result)
# Remove all spaces from the 'course' string.
result = course.replace(' ', '')
print(result)

# 10- Replace 'World' with 'There' in the string 'Hello World'.
result = 'Hello World'.replace('World', 'There')
print(result)

# 11- Split the 'course' string by spaces and convert it into a list.
result = course.split(' ')
print(result)
# Get the sixth element of the split list (indexing starts from zero).
result = result[5]
print(result)
