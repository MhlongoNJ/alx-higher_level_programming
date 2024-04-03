#!/usr/bin/python3
def uppercase(str):
    for Uppercase_String in str:
        if ord(Uppercase_String) >= 97 and ord(Uppercase_String) <= 122:
            Uppercase_String = chr(ord(Uppercase_String) - 32)
            print("{}".format(Uppercase_String), end="")
            print()
