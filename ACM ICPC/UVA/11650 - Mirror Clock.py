# solved
t = int(input())

while t > 0:
    T = input()
    H = int(T[:2])
    M = int(T[3:5])
    M = (60 - M) % 60
    H = 12 - H
    if M != 0:
        H -= 1
    H = (12 + H) % 12
    if H == 0:
        H = 12
    print('%02d:%02d' % (H, M))
    t -= 1
