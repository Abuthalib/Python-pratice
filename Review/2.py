# create a 3*3 matrix

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# for row in matrix1:
#     print(row)

# create two matrices


result_matrix =[]
for i in range(len(matrix1)):
    result_row =[]
    for j in range(len(matrix1[0])):
        result_row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(result_row)

for row in result_matrix:
    print(row)


