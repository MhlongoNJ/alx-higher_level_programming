#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_digit_value = number % -(10)
        print(-(last_digit_value), end="")
    else:
        last_digit_value = number % 10
        print(last_digit_value, end="")
    return abs(last_digit_value)
