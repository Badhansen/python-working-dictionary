# solved
m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))
M = M.symmetric_difference(N)
print(len(M))