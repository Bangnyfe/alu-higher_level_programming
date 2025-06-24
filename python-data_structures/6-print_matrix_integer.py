#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Join all integers in the row into a string separated by spaces
        print(" ".join("{:d}".format(num) for num in row))
