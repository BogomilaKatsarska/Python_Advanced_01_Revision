from collections import deque

'''
STACKS/LIFO/:
-linear data structure
- ss[-1] - peek
*execution stack - when function is calling another functions, which is calling another..*
'''
import collections

ss = [1, 2, 3]

ss.append(5)
ss.pop()
print(ss[-1])
len(ss)

'''
QUEUES/FIFO/:
- We use collections.deque
- We use append() to add to the queue and popleft() to remove from the queue
'''
# BELOW IS SLOW
# qq = []
#
# for i in range(5):
#     qq.append(i)
#
# while len(qq) > 0:
#     print(qq.pop(0))

qq = deque()

for i in range(5):
    qq.append(i)

while len(qq) > 0:
    print(qq.popleft())


