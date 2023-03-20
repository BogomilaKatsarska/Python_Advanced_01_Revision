'''
Inheritance:
Extend the functionality of the code's existing classes to eliminate repetitive code
The capability to inherit properties / methods from other class

1. The super() method:
super().__init__(name, age)

2. Forms of Inheritance
- single - when a child class inherits properties from a single parent class only
- multiple - here we do not use super, but use the name of the parent class
- multilevel - when a child class becomes a parent class for another child class
- hierarchical - when more than one child classes are created from a single parent class

5. Method Resolution Order/MRO/:
It is the order in which methods should be inherited in the presence of multiple inheritance

4. Mixins: 'mix in' extra properties and methods
- A mixin is a class that is implementing a specific set of features that is needed in many different classes
- A mixin is a class which has no data, only methods
- Mixins cannot be instantiated by themselves
- We use mixins to extend functionality
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, date):
        super().__init__(name, age)
        self.date = date


class Manager(Person):
    def __init__(self, name, age, people_managing):
        super().__init__(name, age)
        self.people_managing = people_managing


class Contractor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


class Father:
    def __init__(self):
        self.father_name = 'Nikolay'


class Mother:
    def __init__(self):
        self.mother_name = 'Bogomila'


class Daughter(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)


class RadioMixin():
    def play_song_on_station(self, station_frequency):
        return f'Playing son on a radio frequency {station_frequency}'


