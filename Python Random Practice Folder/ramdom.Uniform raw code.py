# Uniform random number


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


print("Taking input as z, a, m and c")
num = input()
z, a, m, c = map(int, num.split())
rand = []

if gcd(c, m) == 1 and m%4 == 0 and (a-1)%4 == 0:
    while True:
        z = (a * z + c) % m
        u = z / m
        if u in rand:
            # print(len(rand))
            if len(rand) == m:
                print("Full Sequence")
            else:
                print("Not Full Sequence")
            break
        rand.append(u)

print(rand)
