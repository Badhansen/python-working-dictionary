# Solved
import array


n = int(input())
# if you input in one line
x = map(float, input().split(' '))
x = list(x)

# if you input in n lines
#x = []
#for i in range(n):
#    temp = float(input())
#    x.append(temp)


def ucal(u, n):
    if n == 0:
        return 1
    temp = float(u)
    for i in range(1, (n//2)+1):
        temp = temp * (u - i)

    for i in range(1, n//2):
        temp = temp * (u + i)
    return temp


def fact(n):
    f = int(1)
    for i in range(2, n+1):
        f *= i
    return f

y = [[0 for x in range(n+1)] for x in range(n+1)]


y[0][0] = 4.000
y[1][0] = 3.846
y[2][0] = 3.704
y[3][0] = 3.571
y[4][0] = 3.448
y[5][0] = 3.333

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]
        #print(y[j][i])

for i in range(n):
    for j in range(n - i):
        print('{0}   {1}'.format(y[i][j],"\t"))
    print()

value = 27.4
s = (y[2][0] + y[3][0]) / 2
k = 0
if n % 2:
    k = n//2
else:
    k = (n//2) - 1
u = (value - x[k])/ (x[1] - x[0])

for i in range(1, n):
    if i%2 == 0:
        s = s + ((u - 0.5) * ucal(u, i - 1) * y[k][i]) / fact(i)
    else:
        s + (ucal(u, i) * (y[k][i] + y[--k][i]) / (fact(i) * 2))

print('{0} {1} {2} {3}'.format("Value at", value, "is", s))


