# Python List Methods

## Adding an Element to a List

To add an element to the end of a Python list, use the `append()` method.

**Example**

```python
list = ["banana", "grape", "cherry"]
list.append("apple")
print(list)  # ["banana", "grape", "cherry", "apple"]

To insert an element at a specified index in a Python list, use the insert() method.
list = ["banana", "grape", "cherry"]
list.insert(2, "apple")
print(list)  # ["banana", "grape", "apple", "cherry"]

Removing an Element from a List
There are various methods available to remove elements from Python lists.

To remove an element by value, use the remove() method.
list = ["banana", "grape", "cherry"]
list.remove("grape")
print(list)  # ["banana", "cherry"]

To remove an element at a specified index, use the pop() method. If no index is specified, the last element is removed.
list = ["banana", "grape", "cherry"]
list.pop(1)
print(list)  # ["banana", "cherry"]

If no index is given, the last element is removed.
list = ["banana", "grape", "cherry"]
list.pop()
print(list)  # ["banana", "grape"]

The del method can also be used to remove an element at any given index.
list = ["banana", "grape", "cherry"]
del list[2]
print(list)  # ["banana", "grape"]

If the del method is used without an index, the entire list is deleted.
list = ["banana", "grape", "cherry"]
del list
print(list)  # NameError: name 'list' is not defined

In this case, trying to access the list will result in a NameError, indicating that the list is not defined.

Additionally, you can use the clear() method to empty the list. The difference between del and clear() is that with clear(), the list reference remains in memory, whereas with del, the reference is removed.
list = ["banana", "grape", "cherry"]
list.clear()
print(list)  # []

As shown, using print(list) returns [], indicating an empty list. The list object remains in memory and can be used to add elements again.

Copying a List
A list is a class and is treated as a reference type in memory. Therefore, when assigning one list to another, the elements are not copied, but rather the memory address is copied.
a = ["apple", "banana"]
b = ["grape", "cherry"]
a = b

Here, the address of b is assigned to the list a. Thus, both a and b lists refer to the same data at the same memory address (["grape", "cherry"]).

Therefore, any changes made to either a or b will affect both lists.
a = ["apple", "banana"]
b = ["grape", "cherry"]
a = b
b[0] = "updated"
print(a, b)  # output: ['updated', 'cherry'] ['updated', 'cherry']

As shown, after the assignment, updating b[0] does not affect list a because they are different objects with different addresses. Here, only the information inside was copied, not the address.

Another method to copy lists is using the list() method.
a = ["apple", "banana"]
b = ["grape", "cherry"]
a = list(b)
b[0] = "updated"
print(a, b)  # output: ['grape', 'cherry'] ['updated', 'cherry']

Sorting List Elements
To sort list elements, use the sort() method.
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

numbers.sort()  # sorts numerically in ascending order.
letters.sort()  # sorts alphabetically from a to z.

To sort in reverse order, use the reverse=True parameter.
numbers.sort(reverse=True)  # sorts numerically in descending order.
letters.sort(reverse=True)  # sorts alphabetically from z to a.

You can also reverse the order of the list using the reverse() method.
numbers = [1, 10, 5]
letters = ['a', 'g', 's']

numbers.reverse()  # [5, 10, 1]
letters.reverse()  # ['s', 'g', 'a']

Other List Methods
min() and max() Methods
To get the minimum and maximum values in a list, whether numerical or alphabetical, use min() and max() methods.
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

min(numbers)  # 1
max(numbers)  # 16
max(letters)  # y
min(letters)  # a

count() Method
To get the count of repeating elements in a list, use the count() method.
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

numbers.count(10)  # 2
letters.count('a')  # 2
