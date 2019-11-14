#!usr/bin/env python 3

from random import randint


def roll_dice():
    return randint(1, 6)


def check_guess(guess):
    if isinstance(guess, int) and guess >= 1 and guess <= 6:
        return True
    return False


if __name__ == "__main__":
    guess = int(input("Enter your guess\n"))
    valid = check_guess(guess)

    if not valid:
        print(
            "An error occured: your guess can only be a dice value - an integer between 1 and 6 (inclusive)"
        )
    else:
        dice_val = roll_dice()
        if guess == dice_val:
            print("Well done!")
        else:
            print("Sorry, the dice value was " + str(dice_val) + " :(")
