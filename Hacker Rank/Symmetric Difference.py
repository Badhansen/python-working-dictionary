# solved
m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))
D = M ^ N
sorted(D)
for i in D:
    print(i)