n = int(input())

if (n & 1) == 1:
    print("Weird\n")
elif ((n & 1) != 1 & (n >= 2 and n <= 5)):
    print("Not Weird\n")
elif ((n & 1) != 1 & (n >= 6 and n <= 20)):
    print("Weird\n")
else:
    print("Not Weird\n")