matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print("Matrix before transposition:",matrix)


rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("Matrix after transposition:",rez)
