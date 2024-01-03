#!/usr/bin/python3
"""
This is '2-matrix_divided' module.
Functions:
    matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    divide all elements of a matrix by number 'div'.

    args:
        matrix (list of lists): only integers and floats
        div (int, float): divisor
    return:
        new matrix with divided elements
    """
    not_list = "matrix must be a matrix (list of lists) of integers/floats"
    not_same_size = "Each row of the matrix must have the same size"

    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError(not_list)
    else:
        size = len(matrix[0])

    new_matrix = []
    for item in matrix:
        if type(item) is not list:
            raise TypeError(not_list)
        else:
            new = []
            new_matrix.append(new)
            if len(item) != size:
                raise TypeError(not_same_size)
            else:
                for i in item:
                    if type(i) not in [int, float]:
                        raise TypeError(not_list)
                    else:
                        if type(div) not in [int, float]:
                            raise TypeError("div must be a number")
                        else:
                            new.append(float(round(i/div, 2)))

    return new_matrix
