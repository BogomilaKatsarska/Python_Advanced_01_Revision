'''
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

d.) ValueError: is thrown when a function's argument is of an inappropriate type
print(int('xa'))

2. Custom Exceptions:

class CustomError(Exception):
    pass
raise CustomError

3. Catching Exceptions:
try:
except:
finnally: /изпълнява се при всички ситуации/
'''
# print(5 / 0)
# print(', '.join([1, 2, 3]))
# ll = [1, 2]
# print(ll[2])


# def avg(numbers):
#     if not numbers:
#         return None
#     return sum(numbers) / len(numbers)

# print(int('1'))
# print(int(1))
# print(int('xa'))
# print(int(3.14))

def find_sum(numbers_list):
    result = 1
    numbers_list_count = len(numbers_list)
    for i in range(numbers_list_count):
        number = numbers_list[i]
        if number <=5:
            result *= number
        else:
            result /= number
    return result


print(find_sum([1, 4, 5]), 20)
print(find_sum([4, 5, 6, 1, 3]), 10)
print(find_sum([2, 5, 10]), 1)


class CustomError(Exception):
    pass


raise CustomError


class ValueTooSmallError(Exception):
def __init__(self, min_value):
    super().__init__(f'The value must be greater than {min_value}')

raise ValueTooSmallError('The value is too small')


class ValueCannotBeNegativeError(Exception):
    pass


numbers = [int(input()) for _ in range(5)]

for number in numbers:
    if number < 0:
        raise ValueCannotBeNegativeError



class ValueCannotBeNegativeError2(Exception):
    pass


numbers = [1, 2, -3, 5, 4]

try:
    for number in numbers:
        if number < 0:
            raise ValueCannotBeNegativeError2

    print('No exception')
except:
    print('Exception handled')

# one 'try' can have many 'except'-ions
# except: --> most common, but does not provide any additional info
# except IndexError:
# except KeyError:

def raise_exception():
    # x ={}['asd']
    # x=[1][1]
    pass

try:
    raise_exception()
    print('No exception')
except IndexError as err:
    print(f'Index exception handled: {err}')
except KeyError:
    print('Key exception handled')
# except (IndexError, KeyError):
#     print('Index/Key error')
except LookupError:
    print('Lookup exception handled')
except Exception:
    print('General exception handled')


#
try:
    text = input()
    times = int(input())
    print(text * times)
except ValueError:
    print('Variable times must be an integer')