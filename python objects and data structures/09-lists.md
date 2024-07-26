# Python Lists

In Python, a list is a data type used to store multiple items in a single variable. Lists are created using square brackets `[]`. Lists are ordered, mutable, and can contain different data types.

## Creating and Printing Lists

In Python, lists are created using square brackets `[]`. You can store different data types in the same list.

### Examples

List of integers:
```python
my_list1 = [1, 2, 3, 4]
print(my_list1)  # Output: [1, 2, 3, 4]

List containing different data types:
my_list2 = ['one', 2, True, 5.6]
print(my_list2)  # Output: ['one', 2, True, 5.6]

Concatenating Lists
You can concatenate two lists using the + operator.

Example
Concatenating ["one", "two"] and ["three", "four"] results in:
list1 = ["one", "two"]
list2 = ["three", "four"]
numbers = list1 + list2
print(numbers)  # Output: ['one', 'two', 'three', 'four']

List Length
You can find the length of a list using the len() function.

Example
The length of the list ['one', 'two', 'three', 'four'] is:
print(len(numbers))  # Output: 4

Nested Lists
You can store another list inside a list. This is called a nested list.

Example
Nested lists example:
number = [list1, list2]
print(number)  # Output: [['one', 'two'], ['three', 'four']]

Accessing Nested List Elements
To access elements in nested lists, use two indices.

Examples
For the nested list [['one', 'two'], ['three', 'four']]:

The first inner list is:
print(number[0])  # Output: ['one', 'two']

The second inner list is:
print(number[1])  # Output: ['three', 'four']

The first element of the first inner list is:
a = number[0]
print(a[0])  # Output: 'one'

The second element of the first inner list is:
print(a[1])  # Output: 'two'

Alternatively, you can use direct nested indexing:
print(number[0][1])  # Output: 'two'
print(number[1][1])  # Output: 'four'
