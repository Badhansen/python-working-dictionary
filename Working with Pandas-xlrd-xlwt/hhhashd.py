n = int(input())
s = input()
z = [0] * n
for i in range(n):
    if 2 * i <= n:
        if s[:i] == s[i:2 * i]:
            z[i] = i
if max(z) != 0:
    print(n - max(z) + 1)
else:
    print(n)