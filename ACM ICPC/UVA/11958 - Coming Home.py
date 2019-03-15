# Solved
t = int(input())
ts = 1
while t > 0:
    k, T = input().split(' ')
    k = int(k)
    H = int(T[:2])
    M = int(T[3:5])
    H = H*60+M
    mi = 1e9
    for i in range(k):
        K, q = input().split(' ')
        h = int(K[:2])
        m = int(K[3:5])
        q = int(q)
        h = h*60+m
        if h < H:
            h += 1440
        h += q
        mi = min(h, mi)
    print('{0} {1}: {2}'.format('Case', ts, mi-H))
    t -= 1
    ts += 1


