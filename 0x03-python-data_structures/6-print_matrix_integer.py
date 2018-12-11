#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print('{}'.format(matrix[row][column]), end='')
            if column + 1 < len(matrix[row]):
                print(' ', end='')
        print('')
