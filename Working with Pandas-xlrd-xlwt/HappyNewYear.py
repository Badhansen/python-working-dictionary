t = int(input())



for x in range(t):
    s = input()
    cnt = int(0)
    year = int(2018)
    for i in range(11, len(s)):
        if s[i] == '+':
            cnt += 1

    year += cnt
    print("Happy New Year-", end='')
    print(year)
