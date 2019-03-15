from collections import OrderedDict

dic = OrderedDict()
n = int(input())
for i in range(n):

    key = input()
    if not key in dic.keys():
        dic.update({key : 1})
        continue
    dic[key] += 1

print(len(dic.keys()))


print(*dic.values())