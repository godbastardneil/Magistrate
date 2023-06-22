import numpy as np
import math

np.set_printoptions(precision=4)

f = [0.8, 0.5, 0.9, 0.4, 0.7, 0.1, 0.6]
print("F: ", f, end="\n\n")

N = len(f)  # 57
L = math.floor(N/2)  # 28
K = N-L+1       # 30
print("N: ", N, ", L: ", L, ", K: ", K, end="\n\n")
x = []

for i in range(L):
    x.append(f[i:i+K])
x_t = np.transpose(x)
print("X: ")
print(np.matrix(x))
print("X_T: ")
print(x_t, end="\n\n")

s = (x@x_t)
print("S: ")
print(s)

d = np.linalg.matrix_rank(x)
_lambda = np.sort(np.linalg.eigvals(s))[::-1]
u, Sigma, v = np.linalg.svd(x)

print("Собственные значения: ", _lambda)
print("Собственные вектора U: ")
print(u, end="\n\n")

X_elem = []
for i in range(d):
    u_i = u.transpose()[i].copy()
    l = np.sqrt(_lambda[i])
    v_i = (x_t@u_i)/l
    x_i = l * np.matrix(u_i).transpose() @ np.matrix(v_i)
    X_elem.append(x_i)

    print("Собственные вектор u_", i+1, ": ", u_i)
    print("Факторый вектор v_", i+1, ": ", v_i)
    print("X_", i+1, ": ")
    print(x_i, end="\n\n")
print('\n')

XI = []
XI.append(X_elem[0])
XI.append(X_elem[1] + X_elem[2])

print("XI_1: ")
print(XI[0])
print("XI_2: ")
print(XI[1], end="\n\n")


def diagAverage(matrix):
    avg = []
    for i in range(matrix[0].size):
        dCol = i
        dRow = 0
        summ = 0
        cnt = 0
        while dCol >= 0 and dRow < len(matrix):
            summ += matrix[dRow, dCol]
            cnt += 1
            dCol -= 1
            dRow += 1
        avg.append(summ/cnt)
    for i in range(1, len(matrix)):
        dCol = matrix[0].size-1
        dRow = i
        summ = 0
        cnt = 0
        while dCol >= 0 and dRow < len(matrix):
            summ += matrix[dRow, dCol]
            cnt += 1
            dCol -= 1
            dRow += 1
        avg.append(summ/cnt)
    return avg


F1 = diagAverage(XI[0])
F2 = diagAverage(XI[1])

print("Ряд 1: ", np.matrix(F1))
print("Ряд 2: ", np.matrix(F2))

F_get = []
for i in range(len(F1)):
    F_get.append(F1[i]+F2[i])
print("Сумма: ", np.matrix(F_get))
