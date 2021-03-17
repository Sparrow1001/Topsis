import math

M = int(input('число строк '))
N = int(input('число столбцов '))

test_matrix = [[250, 16, 12, 5, 1],
               [200, 16, 8, 3, 2],
               [300, 32, 16, 4, 3],
               [275, 32, 8, 4, 4],
               [225, 16, 16, 2, 5]]



test_weightage = [0.35, 0.25, 0.25, 0.15, 0.15]

test_sign = [1.0, 0.0, 1.0, 1.0, 1.0]


# max - 1
# min - 0

def calculates(input_matrix, input_weightage, input_sign):
    normalised_matrix = []
    temp = []
    square_matrix = []
    sqrt_sum = []
    weighted_matrix = []
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

    K = len(pi)

    for i in range(K - 1):
        for j in range(K - i - 1):
            if pi[j] > pi[j + 1]:
                pi[j], pi[j + 1] = pi[j + 1], pi[j]

    print("\nКонечный список:")
    print(list(reversed(pi)))

if __name__ == '__main__':
    calculates(test_matrix, test_weightage, test_sign)