'''
28:31
1. Syntax Errors(parsing errors) -
e.g.: print('It works'

2. Exceptions(runtime errors)
a.) ZeroDivisionError: division by zero
print(5 / 0)
b.) NameError: name 'x' is not defined
print(x) --- without declaring it before
c.) TypeError: sequence item 0: expected str instance, int found
print(', '.join([1, 2, 3])
d.) IndexError: list index out of range
ll = [1, 2]
print(ll[2])
e.) KeyError: is thrown when key is not found
dd = {
    'k1':'v1',
    'k2':'v2',
}
print(dd['k3']])

'''
# print(5 / 0)
# print(', '.join([1, 2, 3]))
# ll = [1, 2]
# print(ll[2])


# def avg(numbers):
#     if not numbers:
#         return None
#     return sum(numbers) / len(numbers)