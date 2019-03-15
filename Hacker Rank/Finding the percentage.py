test = int(input())
d = {}
while test > 0:
    test -= 1
    name, *marks = input().split()

    d[name] = [float(m) for m in marks]

sk = input()
mark = d[sk]
print ('%.2f'  % (sum(mark)/len(mark)))
