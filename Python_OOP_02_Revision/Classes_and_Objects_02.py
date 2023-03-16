'''
0:59
1. __init__()
- Creates objects with instances, customized to a specific initial state
- Automatically invoked for the newly-created class instance
'''

class Person:
    # class attributes - shared in all instances
    kind = 'mammal'
    skills = ['sleep', 'eat']

    def __init__(self, age, name='Default user'):
        self.age = age
        self.name = name


person_1 = Person(20, "test")
person_2 = Person(10, "test2")
print(person_1.kind)
print(person_2.kind)
