# file = open('my_file.txt')
# file_contents = file.read()
# print(file_contents)
# file.close()

# Good to use with when opening files etc.
# File is closed after it's used so no manual closing.

# with open('my_file.txt', 'w') as file:
#     # file_contents = file.read()
#     # print(file_contents)
#     file.write('Yes I am writing to this file from PYTHON, bro!')
#     # print(file_contents)

# with open('my_file.txt') as f:
#     print(f.read())

#
#
# with open('new_file.txt', mode='w') as f:
#     f.write('Something new.')
#

# Previous Challenge

# with open('../../Desktop/my_file.txt') as my_file:
#     contents = my_file.read()
#     print(contents)
# Why is that so easy...

# Path:
# /home/mundira/Desktop

# Main.py path (absolute path):
# /home/mundira/100-Days-Of-Python/Day-24

# from pathlib import Path
#
# relative = Path('new_file.txt')
# absolute = relative.absolute()
# print(absolute)

#
# import os
#
# # print(os.path.abspath(os.curdir))
# # print(os.path.abspath('main.py'))
#
# for i in range(2):
#     os.chdir('..')
# # Prints absolute path after going up two directories
# with open('Desktop/my_file.txt') as my_file:
#     contents = my_file.read()
#     print(contents)
