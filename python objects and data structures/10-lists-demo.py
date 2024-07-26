# 1- Create a list with the elements "Bmw, Mercedes, Opel, Mazda".
cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

# 2- How many elements are in the list?
result = len(cars)

# 3- What is the first and last element of the list?
result = cars[0]
result = cars[3]
result = cars[-1]

# 4- Replace the value 'Mazda' with 'Toyota'.
# cars[-1] = 'Toyota'
result = cars

# 5- Is 'Mercedes' an element of the list?
result = 'Mercedes' in cars

# 6- What is the value at index -2 of the list?
result = cars[-2]

# 7- Get the first 3 elements of the list.
result = cars[0:3]
result = cars[:3]
result = cars[-2:]

# 8- Replace the last 2 elements of the list with "Toyota" and "Renault".
cars[-2:] = ['Toyota', 'Renault']
result = cars

# 9- Append "Audi" and "Nissan" to the list.
result = cars + ['Audi', 'Nissan']

# 10- Remove the last element of the list.
del cars[-1]
result = cars

# 11- Print the list elements in reverse order.
result = cars[::-1]

# 12- Store the following data in a list:
# 
# studentA: Yiğit Bilgi 2010, (70, 60, 70)
# studentB: Sena Turan 1999, (80, 80, 70)
# studentC: Ahmet Turan 1998, (80, 70, 90)

studentA = ['Yiğit', 'Bilgi', 2010, [70, 60, 70]]
studentB = ['Sena', 'Turan', 1999, [80, 80, 70]]
studentC = ['Ahmet', 'Turan', 1998, [80, 70, 90]]

# 13- Print the list elements.

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} is {2019 - studentA[2]} years old and has an average grade of {(studentA[3][0] + studentA[3][1] + studentA[3][2]) / 3}"

print(result)
