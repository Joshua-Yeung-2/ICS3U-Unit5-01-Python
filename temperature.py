# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on October 2021
# This program is to calculate the temperature


def fahrenheit():
    # This function is to calculate the temperature

    # input
    tc = input("Enter a temperature (℃): ")
    print("")

    # process
    try:
        tc_int = int(tc)
        tf = (9 / 5) * tc_int + 32

        # output
        print("The temperature in degrees Fahrenheit is {}℉.".format(tf))

    except Exception:
        print("sorry, this is not a number")
        print("please try again")

    print("\nDone")


def main():
    # this function just calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()
