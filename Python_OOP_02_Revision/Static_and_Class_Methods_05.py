'''

16:00
1.Instance method - has (self, ...)

2.Static method:
@staticmethod

- it knows nothing about the class or instance it is called on
- it cannot modify object state or class state
- it could be put outside the class, but it is inside the class where it is applicable
- does not take a self parameter

3.Class method:
@classmethod

- it is bound to the class and not to the object of the class
- it can modify a class state that would apply across all the instances of the class
- simply provide a shortcut for creating a new instance objects
- you could easily follow the Don't Repeat Yourself (DRY) principle using the class methods

4. Overriding Using Methods

5. Decorator /@/
'''

from functools import reduce

class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age): #it does not take a self parameter
        return age >= 18

print(Person.is_adult(5))
girl = Person('Amy')
print(girl.is_adult(20))


class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x*y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x/y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(['tomato sauce', 'parmesan', 'pepperoni'])

    @classmethod
    def quatro_formaggi(cls):
        return cls(['mozzarella', 'gorgonzola', 'fontina', 'parmigiano'])


first_pizza = Pizza.pepperoni()
second_pizza = Pizza.quatro_formaggi()


class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {} #self.items = defaultdict(lambda: 0)

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.capacity > 0:
            if item_name not in self.items: #can use python defaultdict
                self.items[item_name] = 0
            self.items[item_name] += 1
            self.capacity -= 1
            return f'{item_name} added to the shop'
        return f'Not enough capacity in the shop'

    def remove_item(self, item_name, amount):
        if item_name in self.items:
            self.items[item_name] -= amount
            self.capacity += amount
            return f'{amount} {item_name} removed from the shop'
        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'