#!/usr/bin/python3

for i in range(100):
    if int(f"{i:02d}"[0]) < int(f"{i:02d}"[1]):
        print(f"{', ' if i > 1 else ''}{i:02d}", end = "")
print()
