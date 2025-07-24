# Python Naming Conventions & CamelCase Reference

## What is CamelCase?

CamelCase is a naming convention in programming where words are joined together without spaces, and each word (except sometimes the first) begins with a capital letter.

### Types of CamelCase:

1. **PascalCase** (UpperCamelCase): First letter is capitalized
   - Examples: `MyVariable`, `CalculateTotal`, `UserAccount`

2. **camelCase** (lowerCamelCase): First letter is lowercase
   - Examples: `myVariable`, `calculateTotal`, `userAccount`

### CamelCase Usage in Different Languages:
- **JavaScript/TypeScript**: Variables and functions use camelCase (`userName`, `getData()`)
- **Java/C#**: Classes use PascalCase (`UserService`), variables use camelCase (`firstName`)
- **Python**: Typically uses snake_case instead (`user_name`)
- **Go**: Public functions use PascalCase (`GetUser`), private use camelCase (`getUser`)

---

## Python's Preferred Style (PEP 8)

Python **doesn't use camelCase** as its primary convention. Instead, Python follows the **snake_case** convention:

### Python Naming Conventions:

#### 1. Variables and Functions: `snake_case` (lowercase with underscores)
```python
user_name = "John"
first_name = "Jane"
total_amount = 100.50

def calculate_total():
    pass

def get_user_data():
    pass

def process_payment_info():
    pass
```

#### 2. Classes: `PascalCase` (UpperCamelCase)
```python
class UserAccount:
    pass

class DatabaseConnection:
    pass

class PaymentProcessor:
    pass
```

#### 3. Constants: `UPPER_SNAKE_CASE`
```python
MAX_SIZE = 100
API_KEY = "your_key_here"
DEFAULT_TIMEOUT = 30
DATABASE_URL = "localhost:5432"
```

### Why Python Uses snake_case:
- **Readability**: `calculate_user_score` is easier to read than `calculateUserScore`
- **PEP 8 Standard**: Python's official style guide recommends it
- **Community Convention**: Most Python code follows this pattern
- **Consistency**: Matches Python's built-in functions like `len()`, `str()`, `print()`

### Exceptions - When You Might See CamelCase in Python:
- Working with APIs that use camelCase
- Using certain libraries that follow different conventions
- Converting code from other languages
- Some third-party libraries may use different conventions

### Quick Reference Examples:

| Type | Convention | Example |
|------|------------|---------|
| Variable | snake_case | `user_age = 25` |
| Function | snake_case | `def get_data():` |
| Class | PascalCase | `class StudentRecord:` |
| Constant | UPPER_SNAKE_CASE | `MAX_USERS = 1000` |
| Private variable | _snake_case | `_internal_data = []` |
| Private method | _snake_case | `def _helper_function():` |

### Pro Tips for Python Programming:
1. **Follow PEP 8**: Use snake_case for variables and functions
2. **Be Consistent**: Stick to one naming convention throughout your project
3. **Make it Readable**: Choose descriptive names like `user_email` instead of `ue`
4. **Use IDE/Editor**: Most Python editors will highlight PEP 8 violations
5. **Practice**: The more you use snake_case, the more natural it becomes

### Tools to Help:
- **pylint**: Checks for PEP 8 compliance
- **black**: Auto-formats Python code according to standards
- **flake8**: Another linting tool for style checking

---