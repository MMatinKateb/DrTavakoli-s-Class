n = int(input('Enter number of rows: '))
m = int(input('Enter number of columns: '))

print('---------------------')

x = []

for i in range(n):
    y = []

    for j in range(m):
        print("Enter [{i}][{j}]: ".format(i = i, j = j), end=" ")
        a = float(input())
        y.append(a)

    x.append(y)

print('---------------------\nMatrix:')
for i in x:
    for j in i:
        print(j, end='\t')
    print()