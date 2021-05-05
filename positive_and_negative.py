#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program tells the user if a number is positive or negative


def main():
    # This function determines if a number is positive or negative

    # Input
    entered_integer = int(input("Enter an integer: "))

    # Process and Output
    if entered_integer > 0:
        print("\n{} is positive.".format(entered_integer))
    elif entered_integer < 0:
        print("\n{} is negative.".format(entered_integer))
    else:
        print("\n{} is zero.".format(entered_integer))
    print("\nDone.")


if __name__ == "__main__":
    main()
