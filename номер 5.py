import numpy as np

data = list(map(int, input().split()))
M, N = data[0], data[1]

#Функция, создающая спиральную матрицу M*N
def matrix(M, N):
    a = np.zeros((M, N))
    a[0][0] = 1
    i = 0
    j = 1
    counter = 1

    while 0 in a:
        while j < N and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            j += 1
        j -= 1
        i += 1

        while i < M and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            i += 1
        i -= 1
        j -= 1

        while j > -1 and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            j -= 1
        j += 1
        i -= 1

        while i > -1 and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            i -= 1
        i += 1
        j += 1
    return a

first_res = matrix(M, N)


def multiplication(first_res):
    for i in range(len(first_res)):
        first_res[i] = np.array(first_res[i]) * (i + 1)
    return first_res


print(multiplication(first_res))
