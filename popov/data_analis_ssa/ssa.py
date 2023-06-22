import numpy as np
import math

f = [
    25.4,
    21.2,
    35.7,
    34.2,
    38.9,
    46.8,
    47.5,
    51.9,
    48.2,
    56.3,
    54.7,
    66.5,
    54.9,
    72.9,
    64.9,
    72.6,
    70.3,
    83.1,
    62.8,
    83.2,
    66.3,
    95.6,
    84.8,
    103.8,
    83.9,
    107.4,
    98.8,
    86,
    121.5,
    105.1,
    72.4,
    119,
    101.6,
    127.4,
    84.8,
    97.2,
    73.8,
    98,
    104.3,
    85.1,
    98.6,
    107.5,
    98.6,
    93.7,
    104.8,
    116.7,
    89.1,
    106.9,
    99.1,
    81.3,
    63.4,
    69.3,
    88.6,
    47.9,
    54.7,
    65.5,
    85.2
]

N = len(f)  # 57
L = math.floor(N/2)  # 28
K = N-L+1       # 30
print(N, L, K)
x = []

for i in range(L):
    x.append(f[i:i+K])
x_t = np.transpose(x)

s = (x@x_t)

d = np.linalg.matrix_rank(x)
_lambda = np.sort(np.linalg.eigvals(s))[::-1]
u, Sigma, v = np.linalg.svd(x)

X_elem = []
for i in range(d):
    u_i = u.transpose()[i].copy()
    l = np.sqrt(_lambda[i])
    v_i = (x_t@u_i)/l
    X_elem.append(l * np.matrix(u_i).transpose() @ np.matrix(v_i))

M = 3
step = round(d/M)
XI = [sum(X_elem[0:step]), sum(X_elem[step:2*step]), sum(X_elem[2*step:N])]

print(len(XI), len(XI[0]), len(XI[0][0]), XI[0][0])

L_ = min(L, K)
K_ = max(L, K)
N_ = L+K-1
print(N, L, K)
