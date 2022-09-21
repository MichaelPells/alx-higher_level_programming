#!/usr/bin/python3

for i in range(100):
    print(f"{i:02d}", end = f"""{', ' if i < 99 else '''
'''}""")
