'''
SOLID
1. Single Responsibility:
- each class is responsible for only one thing and should have only one reason to change

2. Open/Closed (opened for extension, closed for modification):
- software entities like classes, modules and functions should be open for extensions, but closed for modifications

3. Liskov Substitution:
- derived types must be completely substitutable for their base types
- derived class only extends functionalities of the base class
- derived class must not remove base class behavior
- example: Student IS-SUBSTITUTED-FOR Person
- LSP is fundamental to good object-oriented software design because it emphasizes one of its core traits - polymorphism
- it is about creating correct hierarchies so that classes derived from a base one are polymorphic along the parent one

4. Interface Segregation:
- a client should not depend on methods it does not use
- a good way of ensuring this is by separation through multiple inheritance
- can use mixins

5. Dependency Inversion:
- interesting design principle by which we protect our code by making it independent of things that are fragile, volatile or out of control
'''