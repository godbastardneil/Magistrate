M = 3
step = round(10/M)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [sum(a[0:step]), sum(a[step:2*step]), sum(a[2*step:10])]
print(b)
