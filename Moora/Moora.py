import math

M = int(input('число строк '))
N = int(input('число столбцов '))

test_matrix = [[60, 0.4, 2540, 500, 990],
               [6.35, 0.15, 1016, 3000, 1041],
               [6.8, 0.1, 1727.2, 1500, 1676],
               [10, 0.2, 1000, 2000, 965],
               [2.5, 0.1, 560, 500, 915],
               [4.5, 0.08, 1016, 350, 508],
               [3, 0.1, 177, 1000, 920]]

test_weightage = [0.1574, 0.1825, 0.2385, 0.2172, 0.2043]

test_sign = [1.0, 0.0, 1.0, 1.0, 1.0]


# max - 1
# min - 0

def calculates(input_matrix, input_weightage, input_sign):
    normalised_matrix = []
    temp = []
    square_matrix = []
    sqrt_sum = []
    weighted_matrix = []
    v_pos = []
    v_neg = []
    pi = []

    print("Начальная матрица:")
    print(input_matrix)

    # calc sum

    # calc square
    for i in range(M):
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

    # calc normalised matrix
    for i in range(0, N):
        for j in range(0, M):
            temp.append(input_matrix[j][i] / sqrt_sum[i])
        normalised_matrix.append(temp.copy())
        temp.clear()

    print("\nНормализованная матрица:")
    print(normalised_matrix)

    # calc weighted matrix
    for i in range(0, N):
        for j in range(0, M):
            temp.append(normalised_matrix[i][j] * input_weightage[i])
        weighted_matrix.append(temp.copy())
        temp.clear()

    print("\nВзвешенная матрица:")
    print(weighted_matrix)

    summ = 0
    for i in range(M):
        for j in range(N):
            if input_sign[j] == 1.0:
                summ += weighted_matrix[j][i]
            if input_sign[j] == 0.0:
                summ -= weighted_matrix[j][i]
        pi.append(summ)
        summ = 0

    print("\nФинальная матрица")
    print(pi)


if __name__ == '__main__':
    calculates(test_matrix, test_weightage, test_sign)