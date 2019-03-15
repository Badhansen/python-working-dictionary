# Uniform random number


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

rand = []


def uniformbernouli():

    print("Taking input as z, a, m and c and p")
    num = input()
    z, a, m, c, p = num.split()

    z = int(z)
    a = int(a)
    m = int(m)
    c = int(c)
    p = float(p)

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

    flag = True

    if rand[0] <= p:
        print("Yes bernouli random number found")
        flag = False
    if flag:
        print("No bernouli random number is found")


uniformbernouli()
