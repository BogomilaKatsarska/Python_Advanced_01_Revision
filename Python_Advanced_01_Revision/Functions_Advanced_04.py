'''
51:29
def some_func(*args, **kwargs):
    pass

*kwargs allows you to pack keyworded variable length of arguments to a function

*unpacking/packing of elements:
tt = (1, 2, 3)
x, *rest = tt

*Recursion - function calling itself
- Direct recursion
- Indirect recursion
- Execution stack
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

# 1


def get_info(name, age, town):
    return f'This is {name} from {town} and he is {age} years old.'


person_dict = {
    'name': 'George',
    'town': 'Sofia',
    'age': 20,
}

print(get_info(**person_dict))


n = 10


def f1(index, n):
    if index == n:
        return #base case, exit condition
    print(index)
    f1(index=index+1, n=n)


f1(index=0, n=n)


def factorial(m):
    if m == 0 or m == 1:
        return 1
    result = m * factorial(m-1)
    print(f'f({m}) = {result}')

    return result

factorial(10)


# f(n) = f(n-1) + f(n-2)
# f(1) = f(0) = 0
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
print(fibonacci(15))

# Character Premutations


def premute(index, values):
    if index == len(values):
        print(values)
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        premute(index+1, values)
        values[i], values[index] = values[index], values[i]


premute(0, list('abc'))