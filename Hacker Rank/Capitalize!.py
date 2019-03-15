# Solved
line = input().split()


def solve(s):
    s = ' '.join(words[0].upper() + words[1:] for words in line)
    return s

for s in line:
    s = s.capitalize()
    print(s, end=" ")

print(solve(line))