def minion_game(s):
    # your code goes here
    vowel = "AEIOU"
    K = 0
    S = 0
    for i in range(len(s)):
        if s[i] in vowel:
            K += (len(s) - i)
        else:
            S += (len(s) - i)

    if K > S:
        print('{0} {1}'.format("Kevin", K))
    elif S > K:
        print('{0} {1}'.format("Stuart", S))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
