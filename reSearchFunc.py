import re

pas = "Python is the best"
x = re.search("[pyt]", pas)

if x:
    print('yes')
else:
    print('no')