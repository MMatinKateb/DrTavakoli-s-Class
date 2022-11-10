import os

if os.path.exists('test'):
    os.rmdir('test')    # in order to remove a directory we use 'os.rmdir(directory)'
else:
    print('Directory does not exist')