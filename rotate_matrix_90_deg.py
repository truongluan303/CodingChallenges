
def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:

    xlen = len(matrix)
    ylen = len(matrix[0])

    rotated_matrix = [[0] * xlen for i in range(ylen)]

    for i in range(xlen):

        for j in range(ylen):

            rotated_matrix[j][xlen - i - 1] = matrix[i][j]

    return rotate_matrix