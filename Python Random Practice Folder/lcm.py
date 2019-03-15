# Creating a python gcd function
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Creating a python lcm function
def lcm(a, b):
    return (a / gcd(a, b)) * b


# calling the function
g = lcm(6, 8)

print(g)
