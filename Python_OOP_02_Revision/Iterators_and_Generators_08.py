'''
1.Iterators/classes/:
- loops and iterators
- iterator is simply an object that can be iterated upon
- an object will return data, one element at a time
- iterator object must implement two methods, __iter__() and __next__() - iterator protocol

- the FOR LOOP can iterate automatically through the list
- the FOR LOOP can iterate over any iterable

2.Generators/functions/:
- generators are a simple way of creating iterators
- a generator is a function that returns an object(iterator)
- iterator can later be iterated over(one value at a time)
- the yield statement: the difference between yield and return is that the return statement terminates the function entirely
- yield however pauses the function saving all its states and later continues from where on successive
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


class vowels:
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.all_vowels = 'AEOUIYaeouiy'
        self.vowels_list = [el for el in self.text if el in self.all_vowels]
        self.end = len(self.vowels_list) -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return self.vowels_list[index]


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(first_n(5)))


def squares(n):
    current_num = 1
    while current_num <= n:
        yield current_num**2
        current_num += 1

print(list(squares(5)))


class squares_iter:
    def __init__(self, end):
        self.end = end
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        temp = self.start
        self.start += 1
        return temp ** 2


for el in squares_iter(5):
    print(el)


def generate(start, end):
    while start <= end:
        yield start
        start += 1


print(list(generate(1, 10)))


def reverse_text(text):
    current_index = len(text) -1
    while current_index >= 0:
        yield text[current_index]
        current_index -= 1

for char in reverse_text('step'):
    print(char, end='')

