#!usr/bin/env python 3

from random import randint


def roll_dice():
    return randint(1, 6)


def roll_two_die():
    return randint(1, 6) + randint(1, 6)


def check_guess(guess):
    if isinstance(guess, int) and guess >= 1 and guess <= 12:
        return True
    return False


if __name__ == "__main__":
    guess = int(
        input(
            "Enter your guess\nPress 1 for less than 7, 2 for equal to 7, and 3 for greater than 7\n"
        )
    )
    valid = check_guess(guess)

    if not valid:
        print(
            "An error occured: your guess can only be an integer between 1 and 12 (inclusive)"
        )
    else:
        dice_val = roll_two_die()
        if guess == 1 and dice_val < 7:
            print(
                "Dice value was "
                + str(dice_val)
                + "\nWell done! You just doubled your money"
            )
        elif guess == 2 and dice_val == 7:
            print(
                "Dice value was "
                + str(dice_val)
                + "\nWell done! You just tripled your money"
            )
        elif guess == 3 and dice_val > 7:
            print(
                "Dice value was "
                + str(dice_val)
                + "\nWell done! You just doubled your money"
            )
        else:
            print(
                "Dice value was "
                + str(dice_val)
                + "\nThe casino just won your money. Haha go have a free beer and come lose more money"
            )
