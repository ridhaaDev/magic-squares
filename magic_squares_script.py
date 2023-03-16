import math


def get_positive_odd_integer():
    '''
        Get an odd, positive integer from standard input
        Upon invalid user input (negative, 1 or even numbers), re-prompt
    '''
    def is_valid_integer(integer): return integer % 2 != 0 and integer >= 3

    first_input = int(input("Enter an odd, positive integer larger than 1: "))

    if (is_valid_integer(first_input)):
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
            print(str(matrix[row][col]) + "\t", end='')
        print()


def is_magic_square(matrix):
    is_magic = False
    # check verticals
    temp = []
    diags = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if (row == col):
                temp.append(matrix[row][col])
                diags.append(temp)

    # check horizontals

    # check diagonals

    print(diags)
    return is_magic


def create_magic_square(matrix):
    '''
        Takes in an n by n matrix
    '''

    row_length = len(matrix)

    # print(first_row)

    # collision_squares = first_row + last_column + top_edge

    # print("Collision squares: ")
    # print(collision_squares)

    # # Starts top middle
    current_index = [0, math.ceil(row_length / 2)]

    def translate(coords, row_length):
        # first row and last row excludes top edge
        first_row = [f"0, {i}" for i in range(row_length - 1)]
        last_column = [f"{i}, {row_length - 1}" for i in range(1, row_length)]
        top_edge = [f"0, {row_length - 1}"]
        coords_str = f"{coords[0], {coords[1]}}"

        if coords_str in first_row:
            return (coords[row_length], coords[coords[1] + 1])
        elif coords_str in last_column:
            return (coords[row_length], coords[coords[1] + 1])


            # if (current_index[0])

            # while (matrix[current_index[0]] ):


def game_loop():

    magic_order = get_positive_odd_integer()

    # input_numbers = [i for i in range(1, magic_order)]
    matrix = create_matrix(magic_order)
    print(matrix)

    print("RESULT: ", magic_order)
    # pretty_print_matrix(matrix)

    print(create_magic_square(matrix))
    # print("INPUT NUMBERS: ", input_numbers)


game_loop()
