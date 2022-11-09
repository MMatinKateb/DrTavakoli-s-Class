# from numpy import transpose

# mat = [[4, 3, 2],
#        [1, 8, 9]]

# tran = transpose(mat)

# for i in tran:
#     print(list(i))

mat = [[4, 3, 2],
       [1, 8, 9]]

tra = [[0, 0],
       [0, 0], 
       [0, 0]]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        tra[j][i] = mat[i][j]

for i in tra:
    print(i)