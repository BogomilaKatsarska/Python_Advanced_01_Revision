'''
Modules and Python Packages:
- a module is a file consisting of Python code
- they are stored in packages
- a package is a collection of Python modules

1. Built-in Modules: pre-installed
- import -- from collections import deque
- import variations:
a.) import random
print(random.randint(1, 10))
b.) from random import randint
print(randint(1,5))
c.) from random import *

- collision - 2 different objects with the same name in the same file
- in order to rename a function: from random import choice as random_choice

2. External Modules
- external modules are downloaded from the internet using by PIP
- venv = virtual environment
- pip install PACKAGE_NAME
- pip freeze > requirements.txt

3. Custom Modules
- any.py file
from lab.calculate_logarithm import calculate_log
print(calculate_log(1024, 2)
'''
import random

print(random.randint(1, 10))

# -----

import termcolor

print(
    termcolor.colored('It works', 'red',)
)


def perform_operation(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '/':
        if number2 == 0:
            raise ValueError('Cannot divide by zero.')
        return number1 / number2
    elif operation == '*':
        return number1 * number2
    elif operation == '^':
        return number1 ^ number2
    else:
        raise ValueError('Operation must be one of the following: +, - , *, /, ^ .')