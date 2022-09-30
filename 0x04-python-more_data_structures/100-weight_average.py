#!/usr/bin/python3

def weight_average(my_list=[]):
    x = dict(my_list)

    summ = 0

    for i in x:
        summ += i * x[i]

    freq = sum(x.values()) or 1

    return (summ / freq)
