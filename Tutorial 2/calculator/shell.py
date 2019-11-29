#!/usr/bin/env python

from calc_operator import Operator
from calc_add import Add
from calc_subtract import Subtract
from calc_multiply import Multiply
from calc_divide import Divide
import sys


class Shell(object):
    def __init__(self):
        pass

    def exec_operation(self, n, x, y):
        if n == 1:
            return Add(x, y).eval()
        if n == 2:
            return Subtract(x, y).eval()
        if n == 3:
            return Multiply(x, y).eval()
        if n == 4:
            return Divide(x, y).eval()

    def validate_option(self, n):
        if n >= 1 and n <= 4:
            return True
        else:
            return False


if __name__ == "__main__":
    print(
        "Welcome to this simple calculator application\n"
        + "Enter two numbers, then choose an operation (Addition, Subtraction, Multiplication or Division) and this program will return the result of the expression!\n"
        + "Let's get started!\n"
    )
    shell = Shell()
    try:
        x = float(input("Enter a number\n"))
        y = float(input("Enter the next number\n"))
        print("\nGreat! Now choose an operation.\n")
        n = int(
            input(
                "Enter 1 for Addition, 2 for Subtraction, 3 for Multiplication, and 4 for Division\n"
            )
        )
        valid = shell.validate_option(n)
        if valid:
            result = shell.exec_operation(n, x, y)
            print("Awesome! The result of this expression is " + str(result))
        else:
            print("Invalid option - try again.")
    except (ValueError):
        print("Sorry, this application currently accepts number only!")
        sys.exit(0)
