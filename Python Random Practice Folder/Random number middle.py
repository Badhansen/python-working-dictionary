
def digit(number):
    d = []
    while number != 0:
        r = number % 10
        d.append(r)
        number = number // 10
    d.reverse()
    return d


def numbercalculation(number):
    num = 0
    x = 1000
    for i in range(0, 4, 1):
        num = num + (x * number[i])
        x = x // 10

    return num


def solve(number):
    for i in range(10):
        d = []
        r = number ** 2
        print("Square Number ", r)
        d = digit(r)
        number = numbercalculation(d)

        print(i, "th Random Number is ", number)

number = int(input("Please Input a 4 Digit Number"))
solve(number)