A = [[1, 5, 3], # 2 x 3
     [-1, 3, 0]]

B = [[1, 3],    # 3 x 2
     [9, 2],
     [4, 5]]

C = [[0, 0],    # 2 x 2
     [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(A)):
            C[i][j] = C[i][j] + A[i][k] + B[k][j]

for i in C:
    print(i)