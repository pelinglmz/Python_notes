names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1- Add the name "Cenk" to the end of the list.
names.append('Cenk')

# 2- Add the value "Sena" to the beginning of the list.
names.insert(0, 'Sena')

# 3- Remove the name "Deniz" from the list.
names.remove('Deniz')

# 4- What is the index of the name "Deniz"?
index_of_deniz = names.index('Deniz') if 'Deniz' in names else None

# 5- Is "Ali" an element of the list?
is_ali_in_list = 'Ali' in names

# 6- Reverse the elements of the list.
names.reverse()

# 7- Sort the elements of the list alphabetically.
names.sort()

# 8- Sort the years list numerically.
years.sort()

# 9- Convert the string "Chevrolet,Dacia" to a list.
car_str = "Chevrolet,Dacia"
car_list = car_str.split(',')

# 10- What are the largest and smallest elements of the years list?
min_year = min(years)
max_year = max(years)

# 11- How many 1998 values are in the years list?
count_1998 = years.count(1998)

# 12- Clear all elements of the years list.
years.clear()

# 13- Store 3 brand names from the user in a list.
brands = []
for _ in range(3):
    brand = input("Brand: ")
    brands.append(brand)

print("Names:", names)
print("Years:", years)
print("Car List:", car_list)
print("Brands:", brands)
