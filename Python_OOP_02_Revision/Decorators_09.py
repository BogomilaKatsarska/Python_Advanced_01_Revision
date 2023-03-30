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