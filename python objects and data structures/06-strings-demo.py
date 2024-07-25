url = "https://www.torproject.org/download/"
description = "Cybersecurity Course"

# 1- How many characters are there in the 'description' string?
description_length = len(description)

# 2- Extract 'https' from the 'url' string.
protocol = url[:5]  # https

# 3- Extract 'org' from the 'url' string.
Method 1: Using slicing
domain_part = url[12:15]  # org
# Method 2: Using split()
url_parts = url.split('.')
domain_part_split = url_parts[1]  # org
# Method 3: Using negative indexing
domain_part_negative_indexing = url[-11:-8]  # org

# 4- Extract the first 10 and last 10 characters from the 'description' string.
first_part = description[:10]
last_part = description[-10:]

# 5- Reverse the characters in the 'description' string.
reversed_description = description[::-1]

first_name, last_name, age, job = 'Ahmet', 'Kaya', 28, 'developer'

# 6- Print the following statement with the given variables:
#    'My name is Ahmet Kaya, I am 28 years old, and my profession is developer.'
full_description = f'My name is {first_name} {last_name}, I am {age} years old, and my profession is {job}.'

# 7- Replace the 'P' in 'Welcome to Python' with 'p'.
greeting = 'Welcome to Python'
updated_greeting = greeting.replace('P', 'p')

# 8- Print 'xyz' repeated 4 times.
repeated_string = 'xyz ' * 4

print(f"Length of description: {description_length}")
print(f"Protocol from URL: {protocol}")
print(f"Domain part from URL: {domain_part}")
print(f"First part of description: {first_part}")
print(f"Last part of description: {last_part}")
print(f"Reversed description: {reversed_description}")
print(full_description)
print(f"Updated greeting: {updated_greeting}")
print(f"Repeated string: {repeated_string}")
