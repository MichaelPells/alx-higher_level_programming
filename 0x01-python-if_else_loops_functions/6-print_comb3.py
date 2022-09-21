#!/usr/bin/python3

for i in range(100):
    if int(f"{i:02d}"[0]) < int(f"{i:02d}"[1]):
        print("{}{:02d}".format(', ' if i > 1 else '', i), end="")
print()
