#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str:
        return (0)

    db = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman = list(map(lambda n: db[n], list(roman_string.upper())))

    groups = []

    for n in range(0, len(roman)):
        if n == 0:
            groups.append(roman[n])

        elif roman[n] == roman[n - 1]:
            # equal to previous, add to previous
            groups[-1] += roman[n]

        elif roman[n] > roman[n - 1]:
            # greater than previous, negate previous, new group
            groups[-1] = - groups[-1]
            groups.append(roman[n])

        elif roman[n] < roman[n - 1]:
            # less than previous, new group
            groups.append(roman[n])

    return (sum(groups))
