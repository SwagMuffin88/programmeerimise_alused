import math

# Task 1
def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    # Write your code here

    intSum = num_a + num_b
    difference = num_a - num_b

    return intSum, difference

# Task 2
def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    # Write your code here
    division = num_a / num_b
    return division

# Task 3
def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    # Write your code here
    division = num_a // num_b
    return division

# Task 4
def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    # Write your code here
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder

# Task 5
def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    # Write your code here
    average = (num_a + num_b) / 2
    return average

# Task 6
def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    # Write your code here
    circle_area = round(2 * math.pi * radius, 2)
    return circle_area

# Task 7
def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    # Write your code here
    triangle_area = round((math.sqrt(3)/4) * side_length ** 2)
    return round(triangle_area)

# Task 8
def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    # Write your code here
    discriminant = b ** 2 - 4 * a * c
    return discriminant

# Task 9
def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    # Write your code here
    c = abs(math.sqrt(a ** 2 + b ** 2))
    return c

# Task 10
def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    # Write your code here
    b = math.sqrt(abs(a ** 2 - c ** 2))
    return b

if __name__ == '__main__':  # faili käivitamisel on if lause tõene, kood käivitub
    assert sum_and_difference(5, 6) == (11, -1)
    assert float_division(12, 3) == 4.0
    assert integer_division(12, 3) == 4
    assert powerful_operations(2, 2) == (4, 4, 0)
    assert find_average(5, 6) == 5.5
    assert area_of_a_circle(4.0) == 25.13
    # print(round(area_of_a_circle(4.0),2))
    # print(round(area_of_an_equilateral_triangle(5.0),2))
    assert area_of_an_equilateral_triangle(5.0) == 11
    print(calculate_discriminant(1, 2, 3))
    print(calculate_hypotenuse_length(4, 3))
    assert calculate_cathetus_length(4, 5) == 3.0
    print("OK")