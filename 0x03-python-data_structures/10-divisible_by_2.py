#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return (list(map(test, my_list)))


def test(val):
    if val % 2:
        return False
    else:
        return True
