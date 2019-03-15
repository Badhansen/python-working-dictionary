# Solved
n, m = map(int, input().split())
array = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

H = 0

for i in array:
    if i in A:
        H += 1
    if i in B:
        H -= 1

print(H)