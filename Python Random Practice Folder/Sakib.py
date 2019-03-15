# Creating Variables
import math

y = []
f = [[0] * 20] * 20
x = []
print("Enter the value of n (Number of pairs of data values - 1 : \n")


n = int(input())


print("Enter the values of x & y : \n")


for i in range(n+1):
    p = input()
    k, l = p.split()
    x.append(float(k))
    y.append(float(l))

h = float(x[1] - x[0])

print("Derivation of y at initial point", x[0], " is : ")

for j in range(n+1):
    f[0][j] = y[j]


for i in range(1, n+1):
    for j in range(n-i+1):
        f[i][j] = f[i-1][j+1] - f[i-1][j]


s = 0.00

for i in range(1, n+1):
    s = s + math.pow(-1, i+1) * (f[i][0]/i)

dy = float(s/h)
print(dy)
