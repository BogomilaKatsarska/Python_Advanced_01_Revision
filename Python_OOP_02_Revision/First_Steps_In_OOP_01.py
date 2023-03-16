'''
- A single method should complete a single task
1. Scope and Namespace(mapping from names to objects):
- Built-In(names, for example the abs() function)
- Global(names in a module)
- /Enclosing/ - function in the function
- Local(names on a function invocation)
- LEGB

- nonlocal x // global x
2. Basics of OOP
- classes and (individual instances) of objects
- Class may have attributes and methods
'''


# Rhombus of stars

def print_row(size, star_count):
    for row in range(size - star_count):
        print(" ", end="")
    for row in range(1, star_count):
        print("*", end=" ")
    print("*")


size = int(input())

for star_count in range(1, size):
    print_row(size, star_count)
for star_count in range(size, 0, -1):
    print_row(size, star_count)


def first():
    def second():
        x = 5
        print(x)
    second()

first()


class Book:
    def __init__(self, name, author, pages):
        # pages is private instance attribute
        self.__pages = pages
        self.author = author
        self.name = name


book = Book('My book', 'Me', 20)
