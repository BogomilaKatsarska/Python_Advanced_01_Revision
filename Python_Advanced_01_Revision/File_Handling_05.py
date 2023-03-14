'''
1. Python File Object
- io module/input output/
2. Opening a File
3. Reading a File
4. Writing and Creating a File
'''

# Relative paths
#  test/test2.py
# ../main.py

# Absolute paths
# C:\\demos\python-advanced-demos\main.py


# r=read == mode (input from the mentioned file)
# w=open for writing, truncating the file first
# x=create a new file and open it for writing. If it exists - overwrite it
# a=create a new file or append to existing

# file = open('main.py', 'r')
# print(file.readlines())
#
# file = open('sample.txt', 'x')
#
# file = open('sample-a.txt', 'a')
#
#
# file_name = 'text.txt'
# try:
#     open(file_name, 'r')
#     print("File found")
# except FileNotFoundError:
#     print("File not found")
