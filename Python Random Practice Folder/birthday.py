res = 1.00
for i in range(1, 23):
    x = 365 - i
    res = res * (x/365)
    # print(res)

print(1.00 - res)
