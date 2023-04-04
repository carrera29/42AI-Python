import random

print ("""
        This is an interactive guessing game!
    You have to enter a number between 1 and 99 to find out the secret number.
    Type 'exit'to end the game.
                                        Good luck!
    """)

ran_num = random.randint(1, 99)
i = 1
while (True):
    num = input("What's your guess between 1 and 99?\n>> ")
    if num.isalpha():
        if num == "exit":
            break
        else:
            print(f"That's not a number")
    else:
        num = int(num)
        if num <= 0 or num >= 100:
            print("your guess is not between 1 and 99")
        elif num is ran_num:
            print("Congratulations, you've got it!")
            print(f"You won in {i} attempts!")
        elif num > ran_num:
            print("Too high!")
        elif num < ran_num:
            print("Too low!")
        i += 1

