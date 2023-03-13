'''

'''

ll = [1, 2, 3, 4]
print(ll[2])

strings = ['Bogomila', 'Nikolay', 'Mila', 'Ivan']

list_of_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

print(list_of_lists[2])

# 1

n = 5 #rows count
m = 4 #cols count

matrix_of_zeroes = []

for _ in range(n):
    row = []
    matrix_of_zeroes.append(row)
    for _ in range(m):
        row.append(0)

print(matrix_of_zeroes)


# 2.

i, j = [int(x) for x in input().split(', ')]
matrix_demos = []
for _ in range(i):
    row = [int(x) for x in input().split(', ')]
    matrix_demos.append(row)

print(matrix_demos)


