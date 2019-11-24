#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: November 2019
# This program shows functions


def percentage(level):
    # calculates percent
    if level == "4+":
        percent = 97

    elif level == "4":
        percent = 90

    elif level == "4-":
        percent = 83

    elif level == "3+":
        percent = 78

    elif level == "3":
        percent = 74

    elif level == "3-":
        percent = 71

    elif level == "2+":
        percent = 68

    elif level == "2":
        percent = 64

    elif level == "2-":
        percent = 61

    elif level == "1+":
        percent = 58

    elif level == "1":
        percent = 54

    elif level == "1-":
        percent = 51

    elif level == "R":
        percent = 30

    else:
        percent = -1

    return percent


def main():
    # calls other functions
    while True:

        level = input("Enter the level: ")

        calculated_percentage = percentage(level)

        if calculated_percentage == -1:
            print("Undefined percent")
        else:
            print("The mark is {0}%".format(calculated_percentage))

        break


if __name__ == "__main__":
    main()
