list = []

t = int(input())

while t>0:
    s = input().split()

    # input the number
    for i in range(1, len(s)):
        s[i] = int(s[i])

    if s[0] == 'insert':
        list.insert(s[1], s[2])

    elif s[0] == 'print':
        print(list)

    elif s[0] == 'remove':
        list.remove(s[1])

    elif s[0] == 'append':
        list.append(s[1])

    elif s[0] == 'sort':
        list.sort()

    elif s[0] == 'pop':
        list.pop()

    elif s[0] == 'reverse':
        list.reverse()
    t-=1
