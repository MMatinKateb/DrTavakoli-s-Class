import re

pas = "python@3450"
x = re.findall('\d', pas)
y = re.findall('[*]', pas)
print(x, y)