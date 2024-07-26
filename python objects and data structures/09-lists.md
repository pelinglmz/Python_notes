# Python Lists

In Python, a list is a data type used to store multiple items in a single variable. Lists are created using square brackets `[]`. Lists are ordered, mutable, and can contain different data types.

## Creating and Printing Lists

In Python, lists are created using square brackets `[]`. You can store different data types in the same list.

  python
  # List of integers
  my_list1 = [1, 2, 3, 4]
  print(my_list1)  # Output: [1, 2, 3, 4]

  # List containing different data types
  my_list2 = ['one', 2, True, 5.6]
  print(my_list2)  # Output: ['one', 2, True, 5.6]

 Concatenating Lists

 python
  You can concatenate two lists using the + operator.
  list1 = ["one", "two"]
  list2 = ["three", "four"]
  numbers = list1 + list2
  print(numbers)  # Output: ['one', 'two', 'three', 'four']

 List Length

python
  You can find the length of a list using the len() function.
  print(len(numbers))  # Output: 4

 Nested Lists

python
  You can store another list inside a list. This is called a nested list.
  number = [list1, list2]
  print(number)  # Output: [['one', 'two'], ['three', 'four']]

 Accessing Nested List Elements

python
  To access elements in nested lists, use two indices.
  # First inner list
  print(number[0])  # Output: ['one', 'two']

  # Second inner list
  print(number[1])  # Output: ['three', 'four']

  # First element of the first inner list
  a = number[0]
  print(a[0])  # Output: 'one'

  # Second element of the first inner list
  print(a[1])  # Output: 'two'

  # Alternatively, use direct nested indexing
  print(number[0][1])  # Output: 'two'
  print(number[1][1])  # Output: 'four'
