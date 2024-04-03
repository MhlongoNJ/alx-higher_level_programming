#!/usr/bin/python3
def fizzbuzz():
    for FizzBuzzNumbers in range(1, 101):
        if FizzBuzzNumbers % 3 == 0 and FizzBuzzNumbers % 5 == 0:
            print("FizzBuzz ", end="")
        elif FizzBuzzNumbers % 3 == 0:
            print("Fizz ", end="")
        elif FizzBuzzNumbers % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(FizzBuzzNumbers), end="")
