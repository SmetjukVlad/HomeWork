def inp():
    matrix = []
    matrix1 = []
    quantity = int(input('enter the size of the matrix: '))
    for i in range(quantity):
        for q in range(quantity):
            matrix1.append(int(input('enter the value of the matrix elements: ')))
            if q == quantity - 1:
                matrix.append(matrix1)
                matrix1 = []
    return matrix, quantity

def summa(x, quantity):
    sum = 0
    for i in range(quantity):
        for q in range(quantity):
            sum += x[i][q]
    print('Average of matrix elements: ',round(float(sum/quantity/quantity),2))

summa(*inp())






inp()