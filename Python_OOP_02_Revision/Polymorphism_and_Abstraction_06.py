from math import pi
from abc import ABC, abstractmethod

'''
1. POLYMORPHISM:
- based on 'poly' (many) and 'morphism'(forms)
- it is the ability to present the same interface for different underlying forms through the interface of their base class

2. Overloading built in methods

3. Duck Typing
example: we can create a method that calls the sound meow, no matter of what the object which makes the sound is

4. Abstraction:
- Abstract classes are classes that contain one or more abstract methods
- An abstract method is a method that is declared, but contains no implementation
- Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods
- Abstract base classes(ABCs) enforce derived classes to implement particular methods from the base class
- We implement using the abc module
'''


class Shape:
    def get_area(self):
        return None


class Triangle(Shape):
    def __init__(self, a, ha):
        self.a = a
        self.ha = ha

    def get_area(self):
        return 0.5*self.a*self.ha


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return f'pi*{self.r**2}'


class Square(Shape):
    def __init__(self, side):
        self.side = side
0
    def get_area(self):
        return self.side**2

    def __add__(self, other):
        return self.side + other.side

# Below is list of shapes
shapes = [Triangle(3, 6), Triangle(5, 8), Square(3), Square(10)]

for shape in shapes:
    print(shape.get_area())

for obj in Square(), Triangle():
    if type(obj)__name__ == 'Square':
        area = obj.calculate_square_area()
    elif type(obj)__name__ == 'Triangle':
        area = obj.calculate_triangle_area()
    print(area)


class Shape2(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass