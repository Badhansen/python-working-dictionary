# fibonacci number

fibo = []


def fibonacci(num):
    fibo.append(0)
    fibo.append(1)
    fibo.append(1)
    for i in range(3, num):
        fibo.append(fibo[i-1] + fibo[i-2])

# Limit of fibonacci number
print("Enter the limit")
n = int(input())
fibonacci(n)
print(fibo)