k, p =map(int, input().split())
x = 0
for i in range(1, (k + 1)):
    x += int(str(i) + str(i)[::-1])

print(x%p)