#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_list = my_list.copy()
    if idx in range(len(my_list)):
        my_list[idx] = element
    return (my_list)
