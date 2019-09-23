#my solution
#time complexity is o(mn)
# space complexity o(n)

def zeroMatrix(matrix):
    if len(matrix) == 0:
        return 
    n = len(matrix)
    m = len(matrix[0])
    firstRow = set()
    firstColumn = set()
    #first scan for the coordinates of zero
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 0:
                # save row or col to rows or cols to zero set
                firstRow.add(r)
                firstColumn.add(c)
    for row in firstRow:
        for i in range(m):
            matrix[row][i] = 0
    for y in firstColumn:
        for j in range(n):
            matrix[j][y] = 0
    return matrix
        

matrix = [[3,4,5],[1,0,3],[3,4,5]]
print(zeroMatrix(matrix))

def zero_matrix(matrix):
    zero_x = []
    zero_y = []
    for i in range (0, len(matrix)):
        for j in range (0, len(matrix[0])):
            if (matrix[i][j] == 0):
                zero_x.append(i)
                zero_y.append(j)
    zero_x = set(zero_x)
    zero_y = set(zero_y)
    for x in zero_x:
        for i in range (0, len(matrix[0])):
            matrix[x][i] = 0
    for y in zero_y:
        for j in range (0, len(matrix)):
            matrix[j][y] = 0
    return matrix

matrix = [[3,4,5],[1,0,3],[3,4,5]]
print(zero_matrix(matrix))