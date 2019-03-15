# solved
n = int(input())
s = set(map(int, input().split()))

ans = 0

for x in s:
    ans += x
print(ans/len(s))
