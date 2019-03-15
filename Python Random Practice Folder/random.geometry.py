# Uniform random number


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

rand = []


def n():
    for x in rand:
        yield x


def uniform():

    print("Taking input as z, a, m and c")
    num = input()
    z, a, m, c = map(int, num.split())

    if gcd(c, m) == 1 and m%4 == 0 and (a-1)%4 == 0:
        while True:
            z = (a * z + c) % m
            u = z / m
            if u in rand:
                # print(len(rand))
                break
            rand.append(u)
    else:
        print("Please give valid input")


def geometry():
    print("Enter the number of times you want to iterate and Probability : ")

    num = input()
    limit, p = num.split()
    limit = int(limit)
    p = float(p)
    c = 0
    uniform()
    r = n()
    for i in range(limit):
        if r.__next__() >= p:
            c = c+1

    return c

print("the number of unsuccessful attempt  is ", geometry())