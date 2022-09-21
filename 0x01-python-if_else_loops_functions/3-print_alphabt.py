#!/usr/bin/python3

i = 97
while i <= 122:
	print(f"{chr(i) if chr(i) != 'q' and chr(i) != 'e' else ''}", end = "")
	i += 1