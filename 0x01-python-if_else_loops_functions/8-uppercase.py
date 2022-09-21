#!/usr/bin/python3

def uppercase(string):
    for c in string:
        if ord(c) in range(97, 123):
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()


