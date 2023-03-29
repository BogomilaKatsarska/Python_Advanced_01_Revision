'''
1:15
1.Iterators/classes/:
- loops and iterators
- iterator is simply an object that can be iterated upon
- an object will return data, one element at a time
- iterator object must implement two methods, __iter__() and __next__() - iterator protocol

- the FOR LOOP can iterate automatically through the list
- the FOR LOOP can iterate over any iterable

2.Generators/functions/:
- the yield statement
'''


class A:
    def __iter__(self):
        return self

    def __next__(self):
        pass

my_list = [4, 6, 7, 0]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        temp = self.start
        self.start += 1
        return temp


class reverse_iter:
    def __init__(self, iterable_obj):
        self.iterable_obj = iterable_obj
        self.start = len(self.iterable_obj - 1)
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        index = self.start
        self.start -= 1
        return self.iterable_obj[index]
