import math

M = int(input('число строк '))
N = int(input('число столбцов '))

test_matrix = [[250, 16, 12, 5, 1],
               [200, 16, 8, 3, 2],
               [300, 32, 16, 4, 3],
               [275, 32, 8, 4, 4],
               [225, 16, 16, 2, 5]]

test_weightage = [0.35, 0.25, 0.25, 0.15, 0.15]


# max - 1
# min - 0


def calculates(input_matrix, input_weightage, input_sign):
    concordance_thresholdValue = 0
    discordance_thresholdValue = 0
    normalised_matrix = []
    temp = []
    square_matrix = []
    sqrt_sum = []
    weighted_matrix = []
    concordance_matrix = []
    concordance_index = []
    concordance_dominance = []
    discordance_set = []
    discordance_matrix = []
    discordance_max = []
    discordance_dominance = []
    max1 = []
    max2 = []
    discordance_index = []
    result_matrix1 = []
    result_matrix2 = []
    result_matrix_sum_first1 = []
    result_matrix_sum_second1 = []
    result_matrix_sum_first2 = []
    result_matrix_sum_second2 = []
    rank1 = []
    rank2 = []

    print("Начальная матрица:")
    print(input_matrix)

    # calc sum

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


    #calc concordance index
    for i in range(N):
        for j in range(M):
            temp1 = weighted_matrix[i][j]

            for k in range(M):
                if k != j:
                    if temp1 >= weighted_matrix[i][k]:
                        temp.append(1)
                    else:
                        temp.append(0)
        concordance_matrix.append(temp.copy())
        temp.clear()

    print("\nconcordance matrix:")
    print(concordance_matrix)

    summ = 0.0
    for i in range(len(concordance_matrix[0])):
        for j in range(N):
            summ += concordance_matrix[j][i] * input_weightage[j]
        concordance_index.append(summ)
        summ = 0

    print("\nconcordance index")
    print(concordance_index)

    summ = 0
    for elm in concordance_index:
        summ += elm
    concordance_thresholdValue = summ / (M * (M - 1))

    print("\nconcordance_thresholdValue")
    print(concordance_thresholdValue)

    for elems in concordance_index:
        if elems < concordance_thresholdValue:
            concordance_dominance.append(1)
        else:
            concordance_dominance.append(0)

    print("\nconcordance_dominance")
    print(concordance_dominance)


    # calc discordance
    for i in range(N):
        for j in range(len(concordance_matrix[0])):
            if concordance_matrix[i][j] == 0:
                temp.append(1)
            else:
                temp.append(0)
        discordance_set.append(temp.copy())
        temp.clear()

    print("\ndiscordance_set")
    print(discordance_set)


    for i in range(N):
        for j in range(M):
            temp1 = weighted_matrix[i][j]
            for k in range(M):
                if k != j:
                    temp.append(abs(temp1 - weighted_matrix[i][k]))
        discordance_matrix.append(temp.copy())
        temp.clear()

    print("\ndiscordance matrix:")
    print(discordance_matrix)

    # max1

    for i in range(N):
        for j in range(len(discordance_matrix[0])):
            temp.append(discordance_matrix[i][j] * discordance_set[i][j])
        discordance_max.append(temp.copy())
        temp.clear()

    print("\ndiscordance max:")
    print(discordance_max)


    for i in range(len(discordance_matrix[0])):
        for j in range(N):
            temp.append(discordance_max[j][i])
        max1.append(max(temp.copy()))
        temp.clear()

    print("\nmax1")
    print(max1)

    # max2

    for i in range(len(discordance_matrix[0])):
        for j in range(N):
            temp.append(discordance_matrix[j][i])
        max2.append(max(temp.copy()))
        temp.clear()

    print("\nmax2")
    print(max2)

    # discordance index

    for i in range(len(max1)):
        discordance_index.append(max1[i] / max2[i])

    print("\ndiscordance_index")
    print(discordance_index)

    summ = 0
    for elm in discordance_index:
        summ += elm
    discordance_thresholdValue = summ / (M * (M - 1))

    print("\ndiscordance_thresholdValue")
    print(discordance_thresholdValue)

    # discordance dominance

    for elems in discordance_index:
        if elems > discordance_thresholdValue:
            discordance_dominance.append(0)
        else:
            discordance_dominance.append(1)

    print("\ndiscordance_dominance")
    print(discordance_dominance)

    counter = 0

    for i in range(len(concordance_index)):
        if i % M == 0:
            temp.append(0.0)
        temp.append(concordance_index[i])
        if counter == M - 2:
            if i == len(concordance_index) - 1:
                temp.append(0.0)
            result_matrix1.append(temp.copy())
            temp.clear()
            counter = 0
            continue
        counter += 1


    summ = 0
    for i in range(len(result_matrix1[0])):
        for j in range(len(result_matrix1)):
            if i != j:
                summ += result_matrix1[j][i]
        result_matrix_sum_second1.append(summ)
        summ = 0

    summ = 0
    for i in range(len(result_matrix1)):
        for j in range(len(result_matrix1[0])):
            if i != j:
                summ += result_matrix1[i][j]
        result_matrix_sum_first1.append(summ)
        summ = 0


    for i in range(len(result_matrix_sum_first1)):
        rank1.append(result_matrix_sum_first1[i] - result_matrix_sum_second1[i])


    for i in range(len(discordance_index)):
        if i % M == 0:
            temp.append(0.0)
        temp.append(discordance_index[i])
        if counter == M - 2:
            if i == len(discordance_index) - 1:
                temp.append(0.0)
            result_matrix2.append(temp.copy())
            temp.clear()
            counter = 0
            continue
        counter += 1


    summ = 0
    for i in range(len(result_matrix2[0])):
        for j in range(len(result_matrix2)):
            if i != j:
                summ += result_matrix2[j][i]
        result_matrix_sum_second2.append(summ)
        summ = 0

    summ = 0
    for i in range(len(result_matrix2)):
        for j in range(len(result_matrix2[0])):
            if i != j:
                summ += result_matrix2[i][j]
        result_matrix_sum_first2.append(summ)
        summ = 0

    for i in range(len(result_matrix_sum_first2)):
        rank2.append(result_matrix_sum_first2[i] - result_matrix_sum_second2[i])


    print("\nconcordance rank:")
    print(rank1)
    print("\ndiscordance rank:")
    print(rank2)





if __name__ == '__main__':
    calculates(test_matrix, test_weightage, test_sign)