import random

secretNumber = random.randint(1, 20)

print('I think a number between 1 to 20\n')

for guessesTaken in range(1, 7):
    guess = int(input())
    if guess < secretNumber:
        print('You Guess a small number\n')
    elif guess > secretNumber:
        print('You guess a big number\n')
    else:
        break
if guess == secretNumber:
    print('You guess the write number\n')
else:
    print('You guess wrong number\n')
