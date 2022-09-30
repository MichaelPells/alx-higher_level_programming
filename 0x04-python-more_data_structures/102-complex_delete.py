#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    x = list(a_dictionary)

    for k in x:
        if a_dictionary[k] == value:
            del a_dictionary[k]

    return (a_dictionary)
