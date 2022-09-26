#!/usr/bin/env python3
def no_c(my_string):
    your_string = ""

    for i in my_string:
        if i not in ["c", 'C']:
            your_string += i

    return (your_string)
