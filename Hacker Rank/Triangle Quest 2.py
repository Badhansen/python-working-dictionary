a = "123456789"
b = "987654321"
n = int(input())
for i in range(n):
    if i == 0:
        s = ''.join(a[:i + 1])
    else:
        s = ''.join(a[:i + 1] + b[len(b) - i:len(b)])
    print(s)

