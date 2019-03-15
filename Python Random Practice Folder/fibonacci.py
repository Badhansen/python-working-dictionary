# Fibonacci Number Calculation

F = []


def fibonacci(limit):
    F.append(0)
    F.append(1)
    F.append(1)

    for i in range(3, limit):
        F.append(F[i-1] + F[i-2])

    print(F)

print("Please Enter the Sequence length : ")


num = int(input())


print("The Fibonacci Sequence is : ")


fibonacci(num)
