#!/usr/bin/python3

def best_score(a_dictionary):
    if type(a_dictionary) == dict and len(a_dictionary.keys()) > 0:
        x = {a_dictionary[s]: s for s in a_dictionary}
        return (x[max(x)])
    else:
        return (None)
