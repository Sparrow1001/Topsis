import math

M = int(input('число строк '))
N = int(input('число столбцов '))

test_matrix = [[5500, 120, 10, 5],
               [2000, 30, 8, 3],
               [4000, 30, 8, 3],
               [2750, 61, 5, 4],
               [4500, 94, 7, 8]]

#input_matrix = [[input() for _ in range(N)] for _ in range(M)]



def calculates(input_matrix):
    normalised_materix = []
    temp = []
    matr_sum = []
    square_matrix = []
    square_sum = []
    sqrt_matrix = []
    weighted_matrix = []
    si_pos = []
    si_neg = []
    pi = []

    #calc sum

    #calc square
    for i in range(0, M):
        for j in range(N):
            temp.append(input_matrix[i][j]**2)
        square_matrix.append(temp.copy())
        temp.clear()

    #calc square sum
    summ = 0
    for i in range(0, N):
        for j in range(0, M):
            summ += square_matrix[i][j]
        square_sum.append(summ)
        summ = 0





    return (square_sum)



if __name__ == '__main__':
    #print(input_matrix[1][1])
    print(calculates(test_matrix))