#!/usr/bin/python3

def uppercase(string):
    for c in string:
        if ord(c) in range(97, 123):
            r = chr(ord(c) - 32)
        else:
            r = c
        
        print("{}".format(r), end="")
    print()


