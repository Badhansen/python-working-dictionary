from collections import Container

n = int(input())
list = list(set(map(int, input().split())))

list.sort()

print(list[-2])

