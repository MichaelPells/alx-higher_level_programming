#!/usr/bin/python3

i = 97
while i <= 122:
    print("{}".format(chr(i) if chr(i) in ['q', 'e'] else ''), end="")
    i += 1
