import re

pas = "Python3 is good"
x = re.sub('\d', '*', pas)
print(x)