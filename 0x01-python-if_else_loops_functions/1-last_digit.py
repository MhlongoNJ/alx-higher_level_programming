#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
StrNumber = str(number)
LastDigit = StrNumber[-1]
LastDigitNumber = int(LastDigit)
if LastDigitNumber > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, LastDigitNumber))
elif LastDigitNumber == 0:
        print("Last digit of {} is {} and is 0".format(number, LastDigitNumber))
elif LastDigitNumber < 6:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, LastDigitNumber))
