'''
51:29
def some_func(*args, **kwargs):
    pass

*kwargs allows you to pack keyworded variable length of arguments to a function
'''


def f():
    pass


def add(x, y):
    return x+y


print(add(1, 2))


def include_sum(x, *numbers):
    return sum(numbers)


def include_sum_2(*args):
    return sum(args)


print(include_sum(1, 2, 3, 4))
print(include_sum_2(1, 2, 10))
