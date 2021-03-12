import math

M = int(input('число строк '))
N = int(input('число столбцов '))

test_matrix = [[5500, 120, 10, 5],
               [2000, 30, 8, 3],
               [4000, 89, 1, 10],
               [2750, 61, 5, 4],
               [4500, 94, 7, 8]]

test_weightage = [0.4, 0.3, 0.2, 0.2]

test_sign = [0.0, 1.0, 1.0, 1.0]

#print("Введите значения в матрицу")
#input_matrix = [[input() for _ in range(N)] for _ in range(M)]
#print("Введите вес для всех столбцов")
#input_weightage = [input() for _ in range(N)]
#print("Введите определяющие значения")
#input_sign = [input() for _ in range(N)]

#max - 1
#min - 0

def calculates(input_matrix, input_weightage, input_sign):
    normalised_matrix = []
    temp = []
    matr_sum = []
    square_matrix = []
    sqrt_sum = []
    weighted_matrix = []
    v_pos = []
    v_neg = []
    si_pos = []
    si_neg = []
    pi = []

    #calc sum

    # calc square
    for i in range(0, M):
        for j in range(N):
            temp.append(input_matrix[i][j] ** 2)
        square_matrix.append(temp.copy())
        temp.clear()

    # calc square sum
    summ = 0
    for i in range(0, N):
        for j in range(0, M):
            summ += square_matrix[j][i]
        sqrt_sum.append(math.sqrt(summ))
        summ = 0

    #calc normalised matrix
    for i in range(0, N):
        for j in range(0, M):
            temp.append(input_matrix[j][i] / sqrt_sum[i])
        normalised_matrix.append(temp.copy())
        temp.clear()

    #calc weighted matrix
    for i in range(0, N):
        for j in range(0, M):
            temp.append(normalised_matrix[i][j] * input_weightage[i])
        weighted_matrix.append(temp.copy())
        temp.clear()

    #calc V sign
    for i in range(len(weighted_matrix)):
        if input_sign[i] == 1.0:
            v_pos.append(max(weighted_matrix[i]))
        if input_sign[i] == 0.0:
            v_pos.append(min(weighted_matrix[i]))
    for i in range(len(weighted_matrix)):
        if input_sign[i] == 1.0:
            v_neg.append(min(weighted_matrix[i]))
        if input_sign[i] == 0.0:
            v_neg.append(max(weighted_matrix[i]))

    print(weighted_matrix)

    summ = 0
    #calc Si pos
    for i in range(M):
        for j in range(N):
            summ += (weighted_matrix[j][i] - v_pos[j])**2
        si_pos.append(math.sqrt(summ))
        summ = 0

    for i in range(M):
        for j in range(N):
            summ += (weighted_matrix[j][i] - v_neg[j])**2
        si_neg.append(math.sqrt(summ))
        summ = 0

    for





    return (si_neg)



if __name__ == '__main__':
    #print(input_matrix[1][1])
    print(calculates(test_matrix, test_weightage, test_sign))