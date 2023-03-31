'''
0:48
Decorators:
- adding functionality to existing code
- functions returning functions
- our decorator function takes a function as an argument, so let us define a function and pass it to our decorator
'''

# Functions returning functions

def hello_function():
    def say_hi():
        return "HI"
    return say_hi

hello = hello_function()
print(hello())


def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper



@uppercase
def speak():
    return "Hello, I am speaking"

print(speak())


def vowel_filter(func):
    def wrapper():
        letters = func()
        return [letter for letter in letters if letter.lower() in 'aeoui']
    return wrapper


@vowel_filter
def get_letters():
    return ['a', 'b', 'c', 'd', 'e']


def even_numbers(func):
    def wrapper(nums):
        return [num for num in nums if num % 2 == 0]
    return wrapper

@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5, 6]))

# HOW TO CREATE A LOG FILE:

class func_logger:

    _logfile = 'log.out'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.func(*args)

@func_logger
def say_hi(name):
    print(f'Hi, {name}')


@func_logger
def say_bye(name):
    print(f'Bye, {name}')


say_hi("Bogomila")
say_hi("Kaatsarska")
say_bye("Bogomila")
