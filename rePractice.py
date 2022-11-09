import re

password = input('Enter password: ')
print('------------------------')

pattern1 = r"[a-z]"
pattern2 = r"[A-Z]"
pattern3 = r"[0-9]"
pattern4 = r"[$#@!]"

result1 = re.search(pattern1, password)
result2 = re.search(pattern2, password)
result3 = re.search(pattern3, password)
result4 = re.search(pattern4, password)
result5 = (6 <= len(password) <= 12)

if result1 and result2 and result3 and result4 and result5:
    print("Password is valid.")
else:
    print("Password is invalid.")