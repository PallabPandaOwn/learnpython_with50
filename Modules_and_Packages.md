# Modules vs Packages in Python

## Module
A **module** is a single Python file (`.py`) that contains Python code - functions, classes, variables, and executable statements.

## Package
A **package** is a collection of related modules organized in a directory structure. It's essentially a directory that contains multiple Python modules.

---

## Key Differences

| Aspect | Module | Package |
|--------|---------|----------|
| **Structure** | Single `.py` file | Directory containing multiple `.py` files |
| **Purpose** | Contains related functions/classes | Groups related modules together |
| **Import** | `import module_name` | `import package.module` |
| **Identifier** | Requires `__init__.py` (optional in Python 3.3+) | Always requires `__init__.py` |

---

## Examples

### Module Example

**File: `math_utils.py`**
```python
# This is a module
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159

class Calculator:
    def __init__(self):
        self.result = 0
    
    def calculate(self, a, b, operation):
        if operation == 'add':
            return add(a, b)
        elif operation == 'multiply':
            return multiply(a, b)
```

**Usage:**
```python
# Import the entire module
import math_utils
result = math_utils.add(5, 3)

# Import specific functions
from math_utils import add, PI
result = add(5, 3)
print(PI)

# Import with alias
import math_utils as math
result = math.multiply(4, 6)
```

### Package Example

**Directory Structure:**
```
my_package/
├── __init__.py          # Makes it a package
├── math_operations.py   # Module 1
├── string_utils.py      # Module 2
└── data_processing/     # Sub-package
    ├── __init__.py
    ├── csv_handler.py
    └── json_handler.py
```

**File: `my_package/__init__.py`**
```python
# Package initialization file
from .math_operations import add, subtract
from .string_utils import capitalize_words

__version__ = "1.0.0"
__all__ = ['add', 'subtract', 'capitalize_words']
```

**File: `my_package/math_operations.py`**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
```

**File: `my_package/string_utils.py`**
```python
def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    return text[::-1]
```

**Usage:**
```python
# Import from package
from my_package import add, capitalize_words
result = add(10, 5)
text = capitalize_words("hello world")

# Import specific module from package
from my_package.math_operations import multiply
result = multiply(4, 7)

# Import entire module from package
import my_package.string_utils as str_utils
reversed_text = str_utils.reverse_string("Python")

# Import from sub-package
from my_package.data_processing.csv_handler import read_csv
```

---

## The `__init__.py` File

### Purpose:
- **Makes a directory a package** (required in Python < 3.3, optional in 3.3+)
- **Controls what gets imported** when someone imports the package
- **Package initialization code** runs when package is first imported

### Examples:

**Empty `__init__.py`:**
```python
# Just makes the directory a package
```

**With imports:**
```python
# Make specific functions available at package level
from .math_operations import add, subtract

# Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"
```

**With `__all__`:**
```python
from .math_operations import add, subtract, multiply
from .string_utils import capitalize_words, reverse_string

# Controls what gets imported with "from package import *"
__all__ = ['add', 'subtract', 'capitalize_words']
```

## Import Methods

### Module Imports:
```python
# Import entire module
import math_utils

# Import specific items
from math_utils import add, Calculator

# Import with alias
import math_utils as math

# Import all (not recommended)
from math_utils import *
```

### Package Imports:
```python
# Import from package
from my_package import add

# Import module from package
from my_package import math_operations

# Import specific function from specific module
from my_package.math_operations import multiply

# Import sub-package
from my_package.data_processing import csv_handler
```

---

## Practical Example: Creating a Simple Package

### Step 1: Create Directory Structure
```
calculator_package/
├── __init__.py
├── basic_operations.py
├── advanced_operations.py
└── constants.py
```

### Step 2: Create Module Files

**`calculator_package/constants.py`:**
```python
PI = 3.14159265359
E = 2.71828182846
GOLDEN_RATIO = 1.61803398875
```

**`calculator_package/basic_operations.py`:**
```python
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

**`calculator_package/advanced_operations.py`:**
```python
import math
from .constants import PI

def power(base, exponent):
    """Calculate base raised to exponent"""
    return base ** exponent

def square_root(number):
    """Calculate square root"""
    return math.sqrt(number)

def circle_area(radius):
    """Calculate area of circle"""
    return PI * radius ** 2
```

**`calculator_package/__init__.py`:**
```python
"""
Calculator Package - A simple calculator with basic and advanced operations
"""

# Import functions to make them available at package level
from .basic_operations import add, subtract, multiply, divide
from .advanced_operations import power, square_root, circle_area
from .constants import PI, E, GOLDEN_RATIO

# Package metadata
__version__ = "1.0.0"
__author__ = "Python Developer"

# Control what gets imported with "from calculator_package import *"
__all__ = [
    'add', 'subtract', 'multiply', 'divide',
    'power', 'square_root', 'circle_area',
    'PI', 'E', 'GOLDEN_RATIO'
]
```

### Step 3: Usage
```python
# Using the package
from calculator_package import add, multiply, circle_area, PI

result1 = add(10, 5)           # 15
result2 = multiply(4, 6)       # 24
area = circle_area(5)          # 78.54
print(f"PI value: {PI}")       # 3.14159265359

# Or import specific modules
from calculator_package import basic_operations
result = basic_operations.divide(20, 4)  # 5.0
```

---

## Best Practices

### For Modules:
1. **Keep modules focused** - One module, one responsibility
2. **Use descriptive names** - `user_authentication.py` vs `auth.py`
3. **Add docstrings** - Document what the module does
4. **Organize functions logically** - Group related functions together

### For Packages:
1. **Create meaningful `__init__.py`** - Make imports convenient
2. **Use sub-packages** for complex projects
3. **Follow naming conventions** - Use lowercase with underscores
4. **Document package structure** - README files help
5. **Use `__all__`** to control public API

### Project Structure Example:
```
my_project/
├── README.md
├── setup.py
├── requirements.txt
├── my_project/              # Main package
│   ├── __init__.py
│   ├── core/               # Sub-package
│   │   ├── __init__.py
│   │   ├── models.py       # Module
│   │   └── utils.py        # Module
│   ├── api/                # Sub-package
│   │   ├── __init__.py
│   │   ├── routes.py       # Module
│   │   └── validators.py   # Module
│   └── config.py           # Module
└── tests/                  # Test package
    ├── __init__.py
    ├── test_core.py
    └── test_api.py
```

This structure provides clear organization, making your code maintainable and easy to understand!

