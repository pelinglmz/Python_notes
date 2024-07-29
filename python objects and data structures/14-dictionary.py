# Example of cities and license plates
plates = { 'van': 65, 'istanbul': 34 }

# Print the license plate numbers of Van and Istanbul
print(plates['van'])       # 65
print(plates['istanbul'])  # 34

# Add a new city and update an existing city
plates['ankara'] = 6
plates['van'] = 'new value'

print(plates)  # {'van': 'new value', 'istanbul': 34, 'ankara': 6}

# Example of users
users = {
    'sadikturan': {
        'age': 36,
        'roles': ['user'],
        'email': 'sadik@gmail.com',
        'address': 'istanbul',
        'phone': '1234567'
    },
    'cinarturan': {
        'age': 2,
        'roles': ['admin', 'user'],
        'email': 'cinar@gmail.com',
        'address': 'van',
        'phone': '7654321'
    }
}

# Print the first role of cinarturan
print(users['cinarturan']['roles'][0])  # admin

# Print the address of sadikturan
print(users['sadikturan']['address'])  # istanbul

# Print the phone number of sadikturan
print(users['sadikturan']['phone'])  # 1234567

# Print the email address of cinarturan
print(users['cinarturan']['email'])  # cinar@gmail.com

# Print the age of cinarturan
print(users['cinarturan']['age'])  # 2
