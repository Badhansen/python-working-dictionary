# Creating a python prime number generator function

prime = []


def solve(limit):
    dp = [True] * limit
    dp[0] = dp[1] = False
    prime.append(2)
    for i in range(4, limit, 2):
        dp[i] = False

    for i in range(3, limit, 2):
        if dp[i]:
            prime.append(i)
            for j in range(i * i, limit, i):
                dp[j] = False


# User input how many prime you want
print("The limit of generating a prime list : ")
num = int(input())
solve(num)
print(prime)



