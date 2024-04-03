#!/usr/bin/python3
for X_axis in range(0, 10):
    for Y_axis in range(X_axis + 1, 10):
        if X_axis == 8 and Y_axis == 9:
            print("89")
        else:
            print("{}{}, ".format(X_axis, Y_axis), end="")
