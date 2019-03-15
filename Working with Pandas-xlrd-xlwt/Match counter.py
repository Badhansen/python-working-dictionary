t = int(input())


for i in range(t):
    list = input().split()

    n = int(list[0])
    m = int(list[1])
    x = input()
    y = input()
    q = int(input())

    while q > 0 :
        q -= 1
        cnt = int(0)
        l = int(input())
        for j in range(n-l+1):
            c = int(0)
            for k in range(l):
              if x[j+k] == y[k]:
                c += 1
            if c == m:
               cnt += 1
        print(cnt)

