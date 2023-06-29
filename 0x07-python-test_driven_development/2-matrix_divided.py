#!/usr/bin/python3
"""
This is '2-matrix_divided.py' module.
Functions:
    def matrix_divided(matrix, div):
"""
def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.

    Args:
        matrix (list): lists of lists
        div (int, float): the num that will loop throught the matrix
        and start dividng element by element

    Returns:
        list: new_matrix
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element)
        new_matrix.append(new_row)
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        i = 0
        j = 0
        for j in range(len(matrix)):
            for i in range(len(matrix[j])):
                if type(matrix[j][i]) != int and type(matrix[j][i]) != float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                    if type(div) != int and type(div) != float:
                        raise TypeError("div must be a number")
                    res = matrix[j][i] / div
                    res = round(res, 2)
                    new_matrix[j][i] = res
                    
                i += 1
        j += 1
        return new_matrix
