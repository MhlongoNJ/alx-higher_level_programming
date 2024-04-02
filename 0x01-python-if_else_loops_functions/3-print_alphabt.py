#!/usr/bin/python3
for Alphabets in range(ord("a"), ord("z") + 1):
    if chr(Alphabets) != "e" and chr(Alphabets) != "q":
        print("{:c}".format(Alphabets), end="")
