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

# Python Virtual Environment Guide

## What is a Virtual Environment?

A Virtual Environment in Python is an isolated environment that allows you to manage dependencies for different projects separately. It creates an isolated space for your Python project, ensuring that the dependencies of one project don't interfere with another.

### Benefits of Using Virtual Environments:
- **Dependency Isolation**: Each project can have its own set of dependencies
- **Version Management**: Different projects can use different versions of the same package
- **Clean Development**: Avoid conflicts between different project requirements
- **Reproducible Environments**: Easily recreate the same environment on different machines
- **System Protection**: Prevent modifications to system-wide Python installation

## How to Set Up a Virtual Environment

### Method 1: Using `venv` (Recommended - Built into Python 3.3+)

#### 1. Check Python Installation
```bash
python3 --version
# or
python --version
```

#### 2. Create a Virtual Environment
Navigate to your project directory and run:
```bash
# Create a virtual environment named 'env'
python3 -m venv env

# Or give it a custom name
python3 -m venv myproject_env
```

#### 3. Activate the Virtual Environment

**On macOS/Linux:**
```bash
source env/bin/activate
```

**On Windows:**
```bash
# Command Prompt
env\Scripts\activate

# PowerShell
env\Scripts\Activate.ps1
```

#### 4. Verify Activation
When activated, your terminal prompt will show the environment name:
```bash
(env) $ 
```

You can also verify by checking Python path:
```bash
which python3
# Should show: /path/to/your/project/env/bin/python3
```

#### 5. Install Packages
With the virtual environment activated, install packages using pip:
```bash
pip install requests
pip install django
pip install numpy pandas
```

#### 6. List Installed Packages
```bash
pip list
# or
pip freeze
```

#### 7. Create Requirements File
Save your project dependencies:
```bash
pip freeze > requirements.txt
```

#### 8. Install from Requirements File
On another machine or environment:
```bash
pip install -r requirements.txt
```

#### 9. Deactivate the Virtual Environment
When you're done working:
```bash
deactivate
```

### Method 2: Using `virtualenv` (Third-party package)

#### 1. Install virtualenv
```bash
pip install virtualenv
```

#### 2. Create Virtual Environment
```bash
virtualenv env
# or specify Python version
virtualenv -p python3.9 env
```

#### 3. Activate and use (same as venv method)

### Method 3: Using `conda` (For data science projects)

#### 1. Install Anaconda or Miniconda

#### 2. Create Environment
```bash
conda create --name myenv python=3.9
```

#### 3. Activate Environment
```bash
conda activate myenv
```

#### 4. Install Packages
```bash
conda install numpy pandas matplotlib
```

## Best Practices

### 1. Project Structure
```
my_project/
├── env/                 # Virtual environment (don't commit to git)
├── src/                 # Source code
├── tests/               # Test files
├── requirements.txt     # Dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore file
```

### 2. .gitignore for Virtual Environments
Add these lines to your `.gitignore`:
```
# Virtual environments
env/
venv/
.env
.venv
myproject_env/

# Conda environments
conda-meta/
```

### 3. Naming Conventions
- Use `env` or `venv` for simple projects
- Use descriptive names for complex projects: `myproject_env`
- Avoid spaces in environment names

### 4. Environment Management Commands

```bash
# Create environment
python3 -m venv env

# Activate (macOS/Linux)
source env/bin/activate

# Activate (Windows)
env\Scripts\activate

# Install package
pip install package_name

# Install from requirements
pip install -r requirements.txt

# Update pip
pip install --upgrade pip

# Create requirements file
pip freeze > requirements.txt

# Deactivate
deactivate

# Remove environment (just delete the folder)
rm -rf env
```

### 5. Common Issues and Solutions

#### Issue: "python3: command not found"
**Solution**: Use `python` instead of `python3`, or install Python 3

#### Issue: Permission denied on Windows
**Solution**: Run terminal as administrator or enable script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Issue: Environment not activating
**Solution**: Check the activation script path and ensure you're in the correct directory

#### Issue: Packages not found after activation
**Solution**: Ensure the environment is properly activated and check with `which python`

## Virtual Environment vs Global Installation

| Aspect | Virtual Environment | Global Installation |
|--------|-------------------|--------------------|
| **Isolation** | ✅ Isolated per project | ❌ Shared across all projects |
| **Dependencies** | ✅ Project-specific versions | ❌ One version for all projects |
| **Conflicts** | ✅ No package conflicts | ❌ Potential version conflicts |
| **Portability** | ✅ Easy to reproduce | ❌ Hard to replicate exact environment |
| **System Safety** | ✅ No system modifications | ❌ Can affect system Python |

## Conclusion

Virtual environments are essential for Python development. They provide isolation, prevent conflicts, and make your projects more maintainable and portable. Always use virtual environments for your Python projects!

---
