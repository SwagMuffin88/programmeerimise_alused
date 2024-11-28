"""Demonstrate how codestyle should be applied."""


def output_int_value_of(a):
    """
    Convert parameter into integer and print its value.

    :param a: integer string that should be printed
    """
    print(int(a))  # Attempt to convert string into int and then output


def perform_addition_and_print_result(a, b):
    """
    Add two parameters together.

    :param a: first added value
    :param b:  second added value
    """
    c = a + b
    print(c)         # -> The output is called 'Stack Trace'

    #Calling the third function
    output_int_value_of(c)


def start_program():
    # Calling the second function
    perform_addition_and_print_result("The output is called", "'Stack Trace'")

start_program()