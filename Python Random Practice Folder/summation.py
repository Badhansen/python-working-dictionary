def summation(num):
    if num == 1:
        return 1
    else:
        return summation(num - 1) + num

sum = summation(100)
print(sum)
s = 0
for i in range(1, 101):
    s += i
print(s)
