

#mysolution

def rotate_matrix(matrix):
    matrix = matrix[::-1]

    for i in range(len(matrix)):
        for j in range(i):
            #do a swap
            matrix[i][j],matrix[j][i] =  matrix[j][i],matrix[i][j]

    return matrix


print(rotate_matrix([[1,2,3,4],[3,4,5,5],[2,4,5,4],[3,4,5,4]]))

#solution 2 
def rotate_90_clockwise(mat):
    n = len(mat[0])
    mat.reverse()
    new_mat = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_mat[i].append(mat[j][i])

    return new_mat

print(rotate_90_clockwise([[1,2,3,4],[3,4,5,5],[2,4,5,4],[3,4,5,4]]))

def rotate_matrix(matrix):
    n = len(matrix)
    # when matrix is rotated 90 degrees, (i,j) goes to (j,n-i), index starts from 0.
    for i in range(n-1):
        for j in range(min(n-i-2,i)+1):
            matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1],matrix[n-j-1][i] = \
                matrix[n-j-1][i],matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1]
    return matrix

print(rotate_matrix([[1,2,3,4],[3,4,5,5],[2,4,5,4],[3,4,5,4]]))
