# Creating a python gcd function


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# calling the function

g = gcd(0, 0)

print(g)