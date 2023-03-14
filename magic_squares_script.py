

def get_positive_odd_integer():
    '''
        Get an odd, positive integer from standard input
        Upon invalid user input (negative, 1 or even numbers), re-prompt
    '''
    is_valid_integer = lambda integer: integer % 2 != 0 and integer >= 3

    first_input = int(input("Enter an odd, positive integer larger than 1: "))

    if (is_valid_integer(first_input)):
        return first_input
    else:
        print("Incorrect. Please adhere to the required format.")
        return get_positive_odd_integer()
    
def create_matrix(magic_order):
    outer_list = [ [0 for i in range(magic_order)] for i in range(9)]
    return outer_list

def pretty_print_matrix(matrix):
    print(len(matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            print(str(matrix[row][col]) + "\t", end='')
        print()



def game_loop():
    
    magic_order = get_positive_odd_integer()

    # input_numbers = [i for i in range(1, magic_order)]
    matrix = create_matrix(magic_order)

    print("RESULT: ", magic_order)
    pretty_print_matrix(matrix)
    # print("INPUT NUMBERS: ", input_numbers)

game_loop()
