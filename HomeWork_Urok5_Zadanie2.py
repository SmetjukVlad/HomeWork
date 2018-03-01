def inp():
    matrix = []
    matrix1 = []
    for i in range(3):
        for q in range(4):
            matrix1.append(int(input('enter the value of the matrix elements: ')))
            if q == 3:
                matrix.append(matrix1)
                matrix1 = []
    return matrix


def search(matrix):
    p1 = float(input('Enter condition 1: '))
    p2 = float(input('Enter condition 2: '))
    counter = 0
    for i in range(3):
        for j in range(4):
            if matrix[i][j] <= p2 and matrix[i][j] >= p1:
                counter +=1
    print('Number of elements satisfying the condition {}<=a(i,j)<={}: {} '.format(p1,p2,counter))

search(inp())