'''

1. __init__()
- Creates objects with instances, customized to a specific initial state
- Automatically invoked for the newly-created class instance

2. Dunder methods
- __str__(self) - returns a printable string representation of any user defined class
- __repr__(self) - returns a machine-readable representation of any user defined class /only for consoles/
- __dict__ - this is a dictionary containing a module's symbol table
- __doc__ - documentation as the green one here
3. Instance variables vs Class variables
'''

class Person:
    # class attributes - shared in all instances
    '''
    This class is responsible for creating a new person.
    This is used for __doc__ dunder method
    '''
    kind = 'mammal'
    skills = ['sleep', 'eat']

    def __init__(self, age, name='Default user'):
        self.age = age
        self.name = name

    def __str__(self):
        return f'This is {self.name}  and he/she is {self.age} years old.'


person_1 = Person(20, "test")
person_2 = Person(10, "test2")
print(person_1.kind)
print(person_2.kind)
