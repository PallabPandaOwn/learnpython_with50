# Python Sets - Complete Guide

## What is a Set in Python?

A **Set** is a built-in data type in Python that represents an unordered collection of unique elements. Sets are mutable (can be modified) and are based on mathematical set theory.

## Key Characteristics

1. **Unordered**: Elements have no defined order or index
2. **Unique elements**: Automatically removes duplicates
3. **Mutable**: Can add/remove elements after creation
4. **Iterable**: Can loop through elements
5. **No indexing**: Cannot access elements by index like lists

## Creating Sets

### Empty Set
```python
# Empty set
empty_set = set()  # Note: {} creates a dict, not a set
print(type(empty_set))  # <class 'set'>
```

### Set with Initial Values
```python
# Set with initial values
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}
```

### From Other Collections
```python
# From a list (removes duplicates)
my_list = [1, 2, 2, 3, 3, 4]
unique_numbers = set(my_list)  # {1, 2, 3, 4}

# From a string
letters = set("hello")  # {'h', 'e', 'l', 'o'}

# From a tuple
coordinates = set((1, 2, 3, 2))  # {1, 2, 3}
```

## Basic Set Operations

### Adding Elements

```python
fruits = {"apple", "banana"}

# Add single element
fruits.add("orange")
print(fruits)  # {'apple', 'banana', 'orange'}

# Add multiple elements
fruits.update(["grape", "mango"])
print(fruits)  # {'apple', 'banana', 'orange', 'grape', 'mango'}

# Update with another set
fruits.update({"kiwi", "pear"})
```

### Removing Elements

```python
fruits = {"apple", "banana", "orange", "grape"}

# remove() - raises KeyError if element not found
fruits.remove("banana")
print(fruits)  # {'apple', 'orange', 'grape'}

# discard() - no error if element not found
fruits.discard("mango")  # No error even though 'mango' is not in set
fruits.discard("apple")  # Removes 'apple'

# pop() - removes and returns arbitrary element
popped_fruit = fruits.pop()
print(f"Removed: {popped_fruit}")

# clear() - removes all elements
fruits.clear()
print(fruits)  # set()
```

### Checking Membership

```python
fruits = {"apple", "banana", "orange"}

print("apple" in fruits)     # True
print("grape" in fruits)     # False
print("banana" not in fruits)  # False

# Length of set
print(len(fruits))  # 3
```

## Set Operations (Mathematical)

### Union (`|` or `union()`)
Combines all unique elements from both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using operator
result = set1 | set2        # {1, 2, 3, 4, 5}

# Using method
result = set1.union(set2)   # {1, 2, 3, 4, 5}

# Union with multiple sets
set3 = {5, 6, 7}
result = set1.union(set2, set3)  # {1, 2, 3, 4, 5, 6, 7}
```

### Intersection (`&` or `intersection()`)
Returns elements common to both sets.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using operator
result = set1 & set2        # {3, 4}

# Using method
result = set1.intersection(set2)  # {3, 4}

# Intersection with multiple sets
set3 = {2, 3, 4, 7}
result = set1.intersection(set2, set3)  # {3, 4}
```

### Difference (`-` or `difference()`)
Returns elements in first set but not in second set.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using operator
result = set1 - set2        # {1, 2}
result = set2 - set1        # {5, 6}

# Using method
result = set1.difference(set2)    # {1, 2}
```

### Symmetric Difference (`^` or `symmetric_difference()`)
Returns elements in either set, but not in both.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using operator
result = set1 ^ set2        # {1, 2, 5, 6}

# Using method
result = set1.symmetric_difference(set2)  # {1, 2, 5, 6}
```

## Set Relationships

```python
set1 = {1, 2}
set2 = {1, 2, 3, 4}
set3 = {5, 6}

# Subset - all elements of set1 are in set2
print(set1.issubset(set2))      # True
print(set1 <= set2)             # True (alternative syntax)
print(set1 < set2)              # True (proper subset)

# Superset - set2 contains all elements of set1
print(set2.issuperset(set1))    # True
print(set2 >= set1)             # True (alternative syntax)
print(set2 > set1)              # True (proper superset)

# Disjoint - no common elements
print(set1.isdisjoint(set3))    # True
print(set2.isdisjoint(set3))    # True
```

## Common Use Cases

### 1. Removing Duplicates
```python
# Remove duplicates from a list
data = [1, 2, 2, 3, 3, 4, 5, 5]
unique_data = list(set(data))
print(unique_data)  # [1, 2, 3, 4, 5] (order may vary)

# Preserve order while removing duplicates
def remove_duplicates_ordered(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

data = [1, 2, 2, 3, 3, 4, 5, 5]
print(remove_duplicates_ordered(data))  # [1, 2, 3, 4, 5]
```

### 2. Finding Common Elements
```python
# Find common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [3, 4, 5, 9, 10]

common_all = set(list1) & set(list2) & set(list3)  # {4, 5}
common_any_two = set(list1) & set(list2)  # {4, 5}
```

### 3. Fast Membership Testing
```python
# O(1) average case lookup time
valid_user_ids = {100, 101, 102, 103, 104}
user_id = 102

if user_id in valid_user_ids:  # Very fast lookup
    print("Valid user")

# Compare with list lookup (O(n))
valid_user_list = [100, 101, 102, 103, 104]
if user_id in valid_user_list:  # Slower for large lists
    print("Valid user")
```

### 4. Finding Unique Elements Across Collections
```python
# Find elements unique to each list
customers_jan = {"Alice", "Bob", "Charlie", "David"}
customers_feb = {"Bob", "Charlie", "Eve", "Frank"}

# Customers only in January
jan_only = customers_jan - customers_feb  # {"Alice", "David"}

# Customers only in February
feb_only = customers_feb - customers_jan  # {"Eve", "Frank"}

# Customers in both months
both_months = customers_jan & customers_feb  # {"Bob", "Charlie"}
```

## Set Comprehensions

```python
# Basic set comprehension
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Set comprehension with condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}

# Set comprehension from string
vowels_in_sentence = {char.lower() for char in "Hello World" if char.lower() in "aeiou"}
print(vowels_in_sentence)  # {'e', 'o'}
```

## Frozen Sets

For immutable sets, use `frozenset()`:

```python
# Create frozen set
immutable_set = frozenset([1, 2, 3, 4])
print(immutable_set)  # frozenset({1, 2, 3, 4})

# Cannot modify frozen set
# immutable_set.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'

# Can use as dictionary keys (since they're hashable)
set_dict = {
    frozenset([1, 2]): "first set",
    frozenset([3, 4]): "second set"
}

# Frozen sets support all non-mutating operations
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
union_result = fs1 | fs2  # frozenset({1, 2, 3, 4, 5})
```

## Performance Characteristics

| Operation | Average Time Complexity | Worst Case |
|-----------|------------------------|------------|
| Add | O(1) | O(n) |
| Remove | O(1) | O(n) |
| Contains | O(1) | O(n) |
| Length | O(1) | O(1) |
| Union | O(len(s) + len(t)) | O(len(s) + len(t)) |
| Intersection | O(min(len(s), len(t))) | O(len(s) * len(t)) |
| Difference | O(len(s)) | O(len(s) * len(t)) |

## Advanced Examples

### Working with Sets of Sets (using frozenset)
```python
# Sets cannot contain mutable objects, so use frozenset for nested sets
set_of_sets = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([1, 2])  # Duplicate will be ignored
}
print(len(set_of_sets))  # 2
```

### Set Operations with Multiple Sets
```python
sets = [
    {1, 2, 3},
    {2, 3, 4},
    {3, 4, 5},
    {4, 5, 6}
]

# Find intersection of all sets
intersection_all = sets[0]
for s in sets[1:]:
    intersection_all &= s
print(intersection_all)  # {3} (if any)

# Find union of all sets
from functools import reduce
union_all = reduce(lambda x, y: x | y, sets)
print(union_all)  # {1, 2, 3, 4, 5, 6}
```

## When to Use Sets

✅ **Use Sets when you need to:**
- Remove duplicates from a collection
- Perform fast membership testing
- Execute mathematical set operations (union, intersection, etc.)
- Find unique elements across multiple collections
- Work with unordered collections of unique items
- Check for common or different elements between collections

❌ **Don't use Sets when you need to:**
- Maintain order of elements (use list or OrderedDict)
- Access elements by index
- Store duplicate values
- Use mutable objects as elements
- Frequently convert to other data types (performance overhead)

## Best Practices

1. **Use sets for membership testing** when you have many lookups to perform
2. **Convert to set temporarily** for operations, then back to list if needed
3. **Use set comprehensions** for readable filtering and transformation
4. **Consider frozenset** when you need an immutable set or want to use sets as dictionary keys
5. **Be aware of memory overhead** - sets use more memory than lists for small collections
6. **Use appropriate set operations** instead of loops when possible for better performance

Sets are powerful tools for data manipulation and are essential for efficient algorithms involving unique elements and mathematical set operations.
