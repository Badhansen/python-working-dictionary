# Solved
def split_and_join(a):
    # write your code here
    a = a.split(" ")
    a = "-".join(a)
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)