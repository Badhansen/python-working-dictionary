a, b, c, n = [int(input()) for _ in range(4)]
list = [[x,y,z] for x in range(a + 1) for y in range(b + 1) for z in range(c + 1) if x + y + z != n]
print(list)