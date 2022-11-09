A = [[1, 5, 3],
     [-1, 3, 0]]

B = [[1, 3, 2],
     [9, 2, 2]]

C = [[0, 0, 0],
     [0, 0, 0]]

for row in range(len(A)):
    for col in range(len(A[0])):
          C[row][col] = A[row][col] - B[row][col]

for i in C:
     print(i)