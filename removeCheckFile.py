# in order to remove a file use 'os.remove(directory)'
# in order to check if a file exists use 'os.path.exists(directory)'

import os

file = open('test.txt', 'w')    # create a file

if os.path.exists('test.txt'):
    os.remove('test.txt')   # remove file
else:
    print('file does not exist')