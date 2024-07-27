# List Operations in Python

### Finding Minimum and Maximum Values

You can find the minimum and maximum values in a list using the `min()` and `max()` functions.

```python
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)  # 1
val = max(numbers)  # 16
val = max(letters)  # 'y'
val = min(letters)  # 'a'
```

Slicing Lists
You can slice lists to get specific portions.
```python
val = numbers[3:6]  # [16, 4, 9]
val = numbers[:3]   # [1, 10, 5]
val = numbers[4:]   # [4, 9, 10]
```

Modifying List Elements
You can modify elements of a list by assigning new values to specific indices.

```python
numbers[4] = 40  # [1, 10, 5, 16, 40, 9, 10]
```

Adding Elements
You can add elements to the end of the list using append() or insert elements at specific positions using insert().

```python
numbers.append(49)      # [1, 10, 5, 16, 40, 9, 10, 49]
numbers.append(59)      # [1, 10, 5, 16, 40, 9, 10, 49, 59]
numbers.insert(3, 78)   # [1, 10, 5, 78, 16, 40, 9, 10, 49, 59]
numbers.insert(-1, 52)  # [1, 10, 5, 78, 16, 40, 9, 10, 49, 52, 59]
```

Removing Elements
You can remove elements using pop() or remove().

```python
numbers.pop()     # removes last element
numbers.pop(0)    # removes first element
numbers.pop(-1)   # removes last element
numbers.remove(59)  # removes the first occurrence of 59
```

Sorting and Reversing
You can sort lists in ascending order using sort() and reverse their order using reverse().

```python
numbers.sort()     # sorts the list
numbers.reverse()  # reverses the list

letters.sort()     # sorts the list
letters.reverse()  # reverses the list
