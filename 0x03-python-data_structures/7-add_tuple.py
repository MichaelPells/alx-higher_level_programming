#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    A = list(tuple_a)
    B = list(tuple_b)

    A = A + [0, 0]
    B = B + [0, 0]

    return (A[0] + B[0], A[1] + B[1])
