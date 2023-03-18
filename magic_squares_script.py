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

    row_length = len(matrix)

    def new_location(coords, row_length):
        # first row and last column excludes top edge
        first_row = [f"0, {i}" for i in range(row_length - 1)]
        last_column = [f"{i}, {row_length - 1}" for i in range(1, row_length)]
        top_edge = [f"0, {row_length - 1}"]
        bottom_edge = [f"{row_length - 1}, {row_length - 1}"]
        coords_str = f"{coords[0]}, {coords[1]}"

        if bottom_edge in last_column:
          last_column.remove(bottom_edge)

        print(last_column)

        print("Compare")
        print(coords_str, first_row)
        # handle edges
        if coords_str in first_row:
            print("FR")
            return (row_length - 1, coords[1] + 1)
        elif coords_str in last_column:
            print("LC")
            return (coords[0] + 1, 0)
        elif coords in top_edge:
            print("TE")
            return (0, row_length)
        elif coords in bottom_edge:
            print("BE")
            return (1, 0)
        
        print("NORMAL")
        return (coords[0] + 1, coords[1] + 1)

    def new_location_with_collision(matrix, coords, row_length):
        curr_location = new_location(coords, row_length)

        print("Curr location")
        print(curr_location)

        if matrix[curr_location[0]][curr_location[1]] != 0:
            down_coords = (coords[0] + 1, coords[1])
            if (down_coords[0] != 0 and down_coords[1] != 0):
                return False # we are done
            return down_coords
        
        return curr_location

    # # Starts top middle
    current_index = [0, math.ceil((row_length - 1) / 2)]
    current_number = 1

    print("Before")
    print(current_index)
    print(matrix)
    matrix[0][1] = current_number
    print("After")
    

    next_location = new_location_with_collision(matrix, current_index, row_length)

    while next_location != False:
        
        print("START LOOP with: ")
        print(current_index)
        matrix[current_index[0]][current_index[1]] = current_number
        current_number += 1

        next_location = new_location_with_collision(matrix, current_index, row_length)

        pretty_print_matrix(matrix)
        current_index = next_location



    print("Next location", next_location)

    # if (current_index[0])

    # while (matrix[current_index[0]] ):


def game_loop():
    magic_order = get_positive_odd_integer()

    # input_numbers = [i for i in range(1, magic_order)]
    matrix = create_matrix(magic_order)
    print(matrix)

    print(create_magic_square(matrix))
    # print("INPUT NUMBERS: ", input_numbers)


game_loop()
