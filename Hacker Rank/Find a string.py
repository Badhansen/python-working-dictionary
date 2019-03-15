string = input()
sub_string = input()
x = 0
for i in range(0, len(string)-len(sub_string)+1):
    n = 0
    for j in range(0, len(sub_string)):
        if string[i+j] == sub_string[j]:
            n += 1
    if n == len(sub_string):
        x += 1


print(x)

def c(A, x):
    count = 0
    for i in range(len(A) - len(x) + 1):
        if A[i:i + len(x)] == x:
            count += 1
    return count

print(c(string, sub_string))