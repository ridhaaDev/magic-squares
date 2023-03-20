import copy
import math


def get_positive_odd_integer():
    """
    Get an odd, positive integer from standard input
    Upon invalid user input (negative, 1 or even numbers), re-prompt
    """

    def is_valid_integer(integer):
        return integer % 2 != 0 and integer >= 3

    first_input = int(input("Enter an odd, positive integer larger than 1: "))

    if is_valid_integer(first_input):
        return first_input
    else:
        print("Incorrect. Please adhere to the required format.")
        return get_positive_odd_integer()


def create_matrix(magic_order):
    outer_list = [[0 for i in range(magic_order)] for i in range(magic_order)]
    return outer_list


def pretty_print_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(str(matrix[row][col]) + "\t", end="")
        print()


def create_magic_square(matrix):
    """
    Takes in an n by n matrix
    """
    matrix_copy = copy.deepcopy(matrix)
    row_length = len(matrix)

    current_index = 1
    row, col = 0, math.floor(len(matrix) / 2)

    while current_index <= math.pow(current_index, 2):
        matrix_copy[row][col] = current_index
        current_index += 1

        wrap_row, wrap_col = (row - 1) % row_length, (col + 1) % row_length

        if matrix_copy[wrap_row][wrap_col]:
            row += 1
            if row >= row_length:
                break
        else:
            row, col = wrap_row, wrap_col

    return matrix_copy


def main():
    magic_order = get_positive_odd_integer()
    empty_matrix = create_matrix(magic_order)

    magic_square = create_magic_square(empty_matrix)
    print(f"The magic square of {magic_order} is: ")

    pretty_print_matrix(magic_square)


if __name__ == "__main__":
    main()
