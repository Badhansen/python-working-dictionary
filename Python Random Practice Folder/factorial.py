# generating a factorial function
# Loop variant


def factorial(num):
    f = 1
    for i in range(2, num+1):
        f *= i
    return f


def fact(num):
    if num == 1:
        return num
    return num * fact(num-1)

f = fact(5)
print(f)