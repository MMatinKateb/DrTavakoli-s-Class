file = open('test.txt', 'w')    # write file
text = "Python is good\n"
file.write(text)
text2 = ['Python\n', 'C++\n', 'PHP\n']
file.writelines(text2)
file.close()

file = open('test.txt', 'a')    # append file
text = "C++ is good\n"
file.write(text)
file.close()

file = open('test.txt', 'r')    # read file
cont = file.read()
print(cont)
file.close()