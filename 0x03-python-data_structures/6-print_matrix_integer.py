#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for j, y in enumerate(x):
            print("{}{:d}".format(" " if j > 0 else "", y), end="")
        print()
