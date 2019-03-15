# solved
m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))
M = M.intersection(N)
print(len(M))