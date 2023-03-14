'''
1;42
Tuples and Sets
1. (Tuple):
- Tuples are part of the standard language
- Tuples are immutable objects, but the objects inside the tuple are mutable
- Tuples are sequences
- Tuples cannot be changed
- Tupes use parantheses

- .COUNT() - returns the number of times a specified value occurs
- .INDEX() - returns the index of the particular element
2. Set/множества/
- Unique sequence - every element is unique
- Unordered collection of items
- Sets are mutable, so we can add or remove items

- Operators
a.union(b) - a|b
a.intersection(b) - a&b
a.issubset(b)
a.issuperset(b)
a.difference(b)
a.symmetric_difference(b)

- Methods
.add
'''

tt = (1, 2, 3, 1, 1, 1)
print(tt[0])
single_element_tuple = (1,)
print(tt.count(1))
print(tt.index(1))


ss = set()
ss.add(1)
ss.add(2)
ss.add(1)
ss.add(3)

print(ss)

print({x % 5 for x in range(15)})

#1. Record unique names:

n = int(input())
names = {input() for _ in range(n)}
print(names)