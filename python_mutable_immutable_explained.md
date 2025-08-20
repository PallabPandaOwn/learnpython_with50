# Python Mutable vs Immutable Objects - Complete Guide

## What are Mutable and Immutable Objects?

**Mutability** refers to whether an object can be changed after it's created.

- **Mutable**: Objects that can be modified after creation (their state can change)
- **Immutable**: Objects that cannot be changed after creation (their state is fixed)

This concept is fundamental to understanding how Python handles data, memory management, and avoiding common programming pitfalls.

## Immutable Data Types

### 1. **Numbers** (int, float, complex)

```python
# Integer example
x = 5
print(f"x = {x}, id = {id(x)}")  # x = 5, id = 140712234567456

x = x + 1  # Creates a NEW integer object
print(f"x = {x}, id = {id(x)}")  # x = 6, id = 140712234567488 (different!)

# Float example
pi = 3.14
original_id = id(pi)
pi = pi + 0.01  # Creates a new float object
print(f"ID changed: {id(pi) != original_id}")  # True

# Complex number
c = 3 + 4j
original_id = id(c)
c = c + 1  # Creates a new complex object
print(f"ID changed: {id(c) != original_id}")  # True
```

### 2. **Strings**

```python
# String immutability demonstration
name = "Alice"
print(f"Original: {name}, id = {id(name)}")

# String concatenation creates NEW object
name = name + " Smith"
print(f"Modified: {name}, id = {id(name)}")  # Different ID

# String methods return NEW strings
original = "hello"
upper_case = original.upper()  # Returns new string "HELLO"
print(f"Original: {original}")    # Still "hello" - unchanged
print(f"Upper: {upper_case}")     # "HELLO"
print(f"Same object? {original is upper_case}")  # False

# Attempting to modify string directly fails
text = "Python"
# text[0] = 'J'  # TypeError: 'str' object does not support item assignment
```

### 3. **Tuples**

```python
# Tuple immutability
coordinates = (10, 20)
print(f"Original tuple id: {id(coordinates)}")

# Cannot modify tuple elements
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Creating a new tuple
new_coordinates = coordinates + (30,)  # Creates new tuple
print(f"New tuple id: {id(new_coordinates)}")  # Different ID
print(f"Original unchanged: {coordinates}")     # (10, 20)
print(f"New tuple: {new_coordinates}")          # (10, 20, 30)

# Tuple with mutable elements (special case)
mixed_tuple = ([1, 2], [3, 4])
print(f"Tuple id: {id(mixed_tuple)}")

# Can modify the lists INSIDE the tuple
mixed_tuple[0].append(3)
print(f"Modified: {mixed_tuple}")      # ([1, 2, 3], [3, 4])
print(f"Tuple id unchanged: {id(mixed_tuple)}")  # Same ID!

# But cannot reassign tuple elements
# mixed_tuple[0] = [1, 2, 3]  # TypeError
```

### 4. **Frozen Sets**

```python
# Frozen set creation
fs = frozenset([1, 2, 3, 4])
print(f"Frozen set: {fs}")

# Cannot modify frozen set
# fs.add(5)     # AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(1)  # AttributeError: 'frozenset' object has no attribute 'remove'

# Can use frozen sets as dictionary keys
frozen_dict = {
    frozenset([1, 2]): "first",
    frozenset([3, 4]): "second"
}
print(frozen_dict)
```

### 5. **Bytes**

```python
# Bytes are immutable
data = b"hello"
print(f"Bytes: {data}")

# Cannot modify individual bytes
# data[0] = ord('H')  # TypeError: 'bytes' object does not support item assignment

# Creating new bytes object
new_data = data.replace(b"hello", b"Hello")
print(f"Original: {data}")     # b'hello'
print(f"New: {new_data}")      # b'Hello'
```

## Mutable Data Types

### 1. **Lists**

```python
# List mutability
fruits = ["apple", "banana"]
original_id = id(fruits)
print(f"Original list id: {original_id}")

# Modifying the SAME object
fruits.append("orange")
print(f"After append id: {id(fruits)}")      # Same ID!
print(f"Same object? {id(fruits) == original_id}")  # True
print(f"Modified list: {fruits}")

# Various list modifications
fruits[0] = "Granny Smith Apple"  # Item assignment
fruits.extend(["grape", "mango"]) # Adding multiple items
fruits.remove("banana")           # Removing items
fruits.sort()                     # Sorting in place

print(f"Final list: {fruits}")
print(f"Still same object? {id(fruits) == original_id}")  # True
```

### 2. **Dictionaries**

```python
# Dictionary mutability
person = {"name": "Alice", "age": 25}
original_id = id(person)
print(f"Original dict id: {original_id}")

# Modifying the SAME object
person["city"] = "New York"       # Adding new key-value pair
person["age"] = 26                # Updating existing value
person.update({"job": "Engineer", "salary": 75000})  # Bulk update

print(f"Modified dict: {person}")
print(f"Same object? {id(person) == original_id}")  # True

# Dictionary methods that modify in place
person.pop("salary")              # Remove and return value
person.setdefault("country", "USA")  # Add if key doesn't exist

print(f"Final dict: {person}")
```

### 3. **Sets**

```python
# Set mutability
numbers = {1, 2, 3}
original_id = id(numbers)
print(f"Original set id: {original_id}")

# Modifying the SAME object
numbers.add(4)                    # Add element
numbers.update([5, 6, 7])         # Add multiple elements
numbers.discard(1)                # Remove element (no error if not found)

print(f"Modified set: {numbers}")
print(f"Same object? {id(numbers) == original_id}")  # True

# Set operations that modify in place
other_set = {6, 7, 8, 9}
numbers |= other_set              # In-place union
numbers &= {2, 3, 4, 5, 6}        # In-place intersection

print(f"Final set: {numbers}")
```

### 4. **Custom Objects** (by default)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Custom objects are mutable by default
person = Person("Alice", 25)
original_id = id(person)
print(f"Original person: {person}, id: {original_id}")

# Modifying attributes of the SAME object
person.name = "Alice Smith"
person.age = 26
person.city = "New York"  # Adding new attribute

print(f"Modified person: {person}, id: {id(person)}")
print(f"Same object? {id(person) == original_id}")  # True
```

## Visual Comparison with Memory References

```python
# IMMUTABLE EXAMPLE - String
print("=== IMMUTABLE EXAMPLE ===")
x = "hello"
y = x           # Both variables point to same object
print(f"x: {x}, id: {id(x)}")
print(f"y: {y}, id: {id(y)}")
print(f"x is y: {x is y}")  # True - same object

x = x + " world"  # x now points to NEW object
print(f"\nAfter modification:")
print(f"x: {x}, id: {id(x)}")  # New object
print(f"y: {y}, id: {id(y)}")  # Original object unchanged
print(f"x is y: {x is y}")      # False - different objects

print("\n=== MUTABLE EXAMPLE ===")
list1 = [1, 2, 3]
list2 = list1   # Both variables point to same object
print(f"list1: {list1}, id: {id(list1)}")
print(f"list2: {list2}, id: {id(list2)}")
print(f"list1 is list2: {list1 is list2}")  # True - same object

list1.append(4) # Modifies the SAME object
print(f"\nAfter modification:")
print(f"list1: {list1}, id: {id(list1)}")  # Same object
print(f"list2: {list2}, id: {id(list2)}")  # Same object, shows change!
print(f"list1 is list2: {list1 is list2}") # True - still same object
```

## Important Implications

### 1. **Function Arguments**

```python
# With IMMUTABLE objects - safe
def modify_immutable(x):
    print(f"Inside function - before: {x}, id: {id(x)}")
    x = x + 1  # Creates new object, original unchanged
    print(f"Inside function - after: {x}, id: {id(x)}")
    return x

num = 5
print(f"Original: {num}, id: {id(num)}")
result = modify_immutable(num)
print(f"After function: {num}, id: {id(num)}")  # Unchanged!
print(f"Result: {result}")

print("\n" + "="*50)

# With MUTABLE objects - potentially dangerous!
def modify_mutable(lst):
    print(f"Inside function - before: {lst}, id: {id(lst)}")
    lst.append(4)  # Modifies the ORIGINAL object!
    print(f"Inside function - after: {lst}, id: {id(lst)}")

my_list = [1, 2, 3]
print(f"Original: {my_list}, id: {id(my_list)}")
modify_mutable(my_list)
print(f"After function: {my_list}, id: {id(my_list)}")  # Changed!
```

### 2. **Safe vs Unsafe Default Arguments**

```python
# DANGEROUS - Mutable default argument
def add_item_bad(item, target_list=[]):  # BAD! Same list used every time
    target_list.append(item)
    return target_list

# This causes problems
list1 = add_item_bad("apple")
list2 = add_item_bad("banana") 
print(f"list1: {list1}")  # ['apple', 'banana'] - unexpected!
print(f"list2: {list2}")  # ['apple', 'banana'] - same object!
print(f"Same object? {list1 is list2}")  # True

print("\n" + "="*30)

# SAFE - Use None as default
def add_item_good(item, target_list=None):  # GOOD!
    if target_list is None:
        target_list = []  # Create new list each time
    target_list.append(item)
    return target_list

# This works correctly
list3 = add_item_good("apple")
list4 = add_item_good("banana")
print(f"list3: {list3}")  # ['apple']
print(f"list4: {list4}")  # ['banana']
print(f"Same object? {list3 is list4}")  # False
```

### 3. **Copying Objects**

```python
import copy

# Shallow copy with mutable objects
original = [1, 2, [3, 4]]
shallow = copy.copy(original)

print(f"Original: {original}")
print(f"Shallow copy: {shallow}")
print(f"Same object? {original is shallow}")  # False

# Modifying nested mutable object affects both
shallow[2].append(5)
print(f"\nAfter modifying nested list:")
print(f"Original: {original}")     # [1, 2, [3, 4, 5]] - affected!
print(f"Shallow copy: {shallow}")  # [1, 2, [3, 4, 5]]

# Deep copy creates completely independent copy
original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)

deep[2].append(5)
print(f"\nAfter deep copy modification:")
print(f"Original: {original}")  # [1, 2, [3, 4]] - unchanged!
print(f"Deep copy: {deep}")     # [1, 2, [3, 4, 5]]
```

### 4. **Dictionary Keys Requirement**

```python
# Only IMMUTABLE objects can be dictionary keys
d = {}

# These work (immutable)
d["string_key"] = "value"      # String
d[42] = "number"               # Integer
d[(1, 2)] = "tuple"            # Tuple
d[frozenset([1, 2])] = "frozenset"  # Frozen set

print(f"Dictionary: {d}")

# These DON'T work (mutable)
try:
    d[[1, 2]] = "list"  # List - mutable
except TypeError as e:
    print(f"List as key error: {e}")

try:
    d[{1, 2}] = "set"   # Set - mutable
except TypeError as e:
    print(f"Set as key error: {e}")

try:
    d[{"a": 1}] = "dict"  # Dictionary - mutable
except TypeError as e:
    print(f"Dict as key error: {e}")
```

## Memory and Performance Implications

### String Concatenation Performance

```python
import time

# INEFFICIENT - String concatenation (creates many objects)
def slow_string_building(n):
    result = ""
    start = time.time()
    for i in range(n):
        result = result + str(i)  # Creates new string each time!
    end = time.time()
    return end - start

# EFFICIENT - Use list then join
def fast_string_building(n):
    parts = []  # Mutable list
    start = time.time()
    for i in range(n):
        parts.append(str(i))  # Modifies same list
    result = "".join(parts)   # Single string creation
    end = time.time()
    return end - start

# Performance comparison
n = 5000
slow_time = slow_string_building(n)
fast_time = fast_string_building(n)

print(f"Slow method (string concat): {slow_time:.4f} seconds")
print(f"Fast method (list + join): {fast_time:.4f} seconds")
print(f"Speed improvement: {slow_time/fast_time:.1f}x faster")
```

## Special Cases and Edge Cases

### 1. **Integer Caching**

```python
# Python caches small integers (-5 to 256)
a = 100
b = 100
print(f"a is b: {a is b}")  # True - same cached object
print(f"id(a): {id(a)}, id(b): {id(b)}")  # Same ID

# Large integers are not cached
a = 1000
b = 1000
print(f"a is b: {a is b}")  # Usually False (implementation dependent)
print(f"id(a): {id(a)}, id(b): {id(b)}")  # Different IDs

# But if created together, they might be same
c = d = 1000
print(f"c is d: {c is d}")  # True - assigned together
```

### 2. **String Interning**

```python
# Python interns some strings
s1 = "hello"
s2 = "hello"
print(f"s1 is s2: {s1 is s2}")  # True - interned

# Not all strings are interned
s3 = "hello world!"
s4 = "hello world!"
print(f"s3 is s4: {s3 is s4}")  # Might be False

# Force interning
import sys
s5 = sys.intern("hello world!")
s6 = sys.intern("hello world!")
print(f"s5 is s6: {s5 is s6}")  # True - forced interning
```

### 3. **Tuple with Mutable Elements**

```python
# Tuple itself is immutable, but can contain mutable objects
t = ([1, 2], {"a": 1})
print(f"Original tuple: {t}")

# Cannot change tuple structure
# t[0] = [3, 4]  # TypeError

# But can modify mutable elements inside
t[0].append(3)      # Modify list inside tuple
t[1]["b"] = 2       # Modify dict inside tuple
print(f"Modified tuple: {t}")  # ([1, 2, 3], {'a': 1, 'b': 2})

# This affects hashability
try:
    hash(t)  # This will fail because tuple contains mutable objects
except TypeError as e:
    print(f"Hash error: {e}")
```

## Creating Immutable Custom Classes

```python
# Creating an immutable class using __slots__ and properties
class ImmutablePoint:
    __slots__ = ('_x', '_y')  # Prevent adding new attributes
    
    def __init__(self, x, y):
        object.__setattr__(self, '_x', x)  # Bypass __setattr__
        object.__setattr__(self, '_y', y)
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __setattr__(self, name, value):
        raise AttributeError(f"Cannot modify immutable object")
    
    def __repr__(self):
        return f"ImmutablePoint({self.x}, {self.y})"
    
    def __hash__(self):
        return hash((self.x, self.y))

# Usage
point = ImmutablePoint(3, 4)
print(point)  # ImmutablePoint(3, 4)

# These will fail
try:
    point.x = 5
except AttributeError as e:
    print(f"Modification error: {e}")

try:
    point.z = 10  # Try to add new attribute
except AttributeError as e:
    print(f"Addition error: {e}")

# Can be used as dictionary key
point_dict = {point: "origin point"}
print(point_dict)
```

## Best Practices

### 1. **Defensive Copying**

```python
class DataProcessor:
    def __init__(self):
        self.data = []
    
    def add_data(self, items):
        # Make a copy to avoid external modification
        self.data.extend(items.copy() if hasattr(items, 'copy') else list(items))
    
    def get_data(self):
        # Return a copy to prevent external modification
        return self.data.copy()

# Usage
processor = DataProcessor()
my_list = [1, 2, 3]
processor.add_data(my_list)

# External modification doesn't affect processor
my_list.append(4)
print(f"Processor data: {processor.get_data()}")  # [1, 2, 3] - unaffected

# Getting data returns copy
data_copy = processor.get_data()
data_copy.append(5)
print(f"Processor data: {processor.get_data()}")  # [1, 2, 3] - still unaffected
```

### 2. **Using Immutable Collections**

```python
# Using namedtuple for immutable records
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
person1 = Person("Alice", 30, "New York")

print(person1)  # Person(name='Alice', age=30, city='New York')
print(person1.name)  # Access by name

# Cannot modify
try:
    person1.age = 31
except AttributeError as e:
    print(f"Modification error: {e}")

# Create new instance with changes
person2 = person1._replace(age=31)
print(person2)  # Person(name='Alice', age=31, city='New York')

# Using dataclass with frozen=True
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutableStudent:
    name: str
    grade: int
    subjects: tuple  # Use tuple instead of list for immutability

student = ImmutableStudent("Bob", 85, ("Math", "Science"))
print(student)

# Cannot modify
try:
    student.grade = 90
except Exception as e:
    print(f"Frozen dataclass error: {e}")
```

## When to Use Mutable vs Immutable

### Use **Immutable** when:

✅ **Thread Safety**: Multiple threads accessing the same data  
✅ **Dictionary Keys**: Need to use objects as dictionary keys  
✅ **Caching/Memoization**: Hashable objects for function result caching  
✅ **Default Arguments**: Function parameters that shouldn't change  
✅ **Configuration**: Settings that shouldn't be modified accidentally  
✅ **Mathematical Objects**: Coordinates, complex numbers, etc.  

### Use **Mutable** when:

✅ **Frequent Updates**: Objects that change often during program execution  
✅ **Performance**: Avoiding object creation overhead  
✅ **Collections**: Growing/shrinking collections of items  
✅ **State Management**: Objects representing changing application state  
✅ **Algorithms**: In-place sorting, modifications, etc.  

## Summary Table

| Aspect | Immutable | Mutable |
|--------|-----------|---------|
| **Can be modified?** | ❌ No | ✅ Yes |
| **Memory efficiency** | ➖ Creates new objects | ✅ Modifies in place |
| **Thread safety** | ✅ Inherently safe | ❌ Requires synchronization |
| **Dictionary keys** | ✅ Can be used | ❌ Cannot be used |
| **Function arguments** | ✅ Safe (no side effects) | ⚠️ Can cause side effects |
| **Hashable** | ✅ Usually yes | ❌ Usually no |
| **Examples** | str, int, tuple, frozenset | list, dict, set, custom objects |

Understanding mutability is crucial for writing correct, efficient, and maintainable Python code. It affects everything from function design to data structure choice and performance optimization.
