# Provided students dictionary example
students = {
    '120': {
        'name': 'Ali',
        'surname': 'Yilmaz',
        'phone': '532 000 00 01'
    },
    '125': {
        'name': 'Can',
        'surname': 'Korkmaz',
        'phone': '532 000 00 02'
    },
    '128': {
        'name': 'Volkan',
        'surname': 'Yukselen',
        'phone': '532 000 00 03'
    },
}

# Task 1: Save the provided students' information into a dictionary using the information obtained from the user.
students = {}

number = input("Student ID: ")
name = input("Student name: ")
surname = input("Student surname: ")
phone = input("Student phone: ")

students.update({
    number: {
        'name': name,
        'surname': surname,
        'phone': phone 
    }
})

number = input("Student ID: ")
name = input("Student name: ")
surname = input("Student surname: ")
phone = input("Student phone: ")

students.update({
    number: {
        'name': name,
        'surname': surname,
        'phone': phone 
    }
})

number = input("Student ID: ")
name = input("Student name: ")
surname = input("Student surname: ")
phone = input("Student phone: ")

students.update({
    number: {
        'name': name,
        'surname': surname,
        'phone': phone 
    }
})

print('*'*50)

# Task 2: Get the student ID from the user and display the corresponding student information.
studentID = input('Student ID: ')
student = students.get(studentID, "Student not found")
print(student)

if student != "Student not found":
    print(f"The student with ID {studentID} is named {student['name']}, their surname is {student['surname']}, and their phone number is {student['phone']}")
else:
    print("Student not found")
